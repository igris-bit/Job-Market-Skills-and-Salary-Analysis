
from functools import lru_cache
from pathlib import Path
import os
import re

import pandas as pd
from flask import Flask, jsonify, render_template, request

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "naukri_data_science_jobs_india.csv"
EXPECTED_COLUMNS = [
    "Job_Role",
    "Company",
    "Location",
    "Job Experience",
    "Skills/Description",
]
SKILL_ALIASES = {
    "python programming": "python",
    "py": "python",
    "js": "javascript",
    "ml": "machine learning",
    "machine-learning": "machine learning",
    "deep-learning": "deep learning",
    "sql server": "sql server",
    "powerbi": "power bi",
    "power-bi": "power bi",
    "ms excel": "excel",
}
SKILL_IGNORES = {"skills", "it skills", "skill", "technical skills"}

app = Flask(__name__)
# The dashboard is served by this same Flask app, so broad CORS access is unnecessary.


@lru_cache(maxsize=1)
def load_data():
    """Read and clean the CSV once per process, then reuse the cached DataFrame."""
    if not DATASET_PATH.is_file():
        raise FileNotFoundError(
            f"Dataset not found at {DATASET_PATH.name}. Ensure the CSV is included in the deployment."
        )

    df = pd.read_csv(DATASET_PATH, low_memory=False)
    missing = [column for column in EXPECTED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing)}")

    df = df[EXPECTED_COLUMNS].copy()
    for column in EXPECTED_COLUMNS:
        df[column] = df[column].fillna("").astype(str).str.strip()

    df = df[(df["Job_Role"] != "") & (df["Company"] != "")]
    df = df.drop_duplicates().reset_index(drop=True)
    return df


def count_values(series, limit=10):
    return series[series.astype(str).str.strip().ne("")].value_counts().head(limit).to_dict()


def extract_skills(df, limit=15):
    skills = []
    for value in df["Skills/Description"]:
        for raw_skill in value.split(","):
            skill = re.sub(r"\s+", " ", raw_skill).strip().lower()
            if not skill or skill in SKILL_IGNORES:
                continue
            skill = SKILL_ALIASES.get(skill, skill)
            skills.append(skill)
    return pd.Series(skills, dtype="string").value_counts().head(limit).to_dict()


def extract_experience(df):
    ranges = []
    for value in df["Job Experience"]:
        match = re.fullmatch(r"\s*(\d+)\s*-\s*(\d+)\s*", value)
        if match:
            minimum, maximum = map(int, match.groups())
            if minimum <= maximum:
                ranges.append((minimum, maximum))

    if not ranges:
        return {
            "valid_records": 0,
            "average_minimum": None,
            "average_maximum": None,
        }

    return {
        "valid_records": len(ranges),
        "average_minimum": round(sum(item[0] for item in ranges) / len(ranges), 2),
        "average_maximum": round(sum(item[1] for item in ranges) / len(ranges), 2),
    }


def location_tokens(df):
    """Return normalized location choices while preserving slash-separated city names."""
    found = set()
    for value in df["Location"]:
        for chunk in value.split(","):
            chunk = chunk.strip()
            if chunk:
                found.add(chunk)
    return sorted(found, key=str.casefold)


def filter_jobs(df, role="", location="", company=""):
    # regex=False makes user-entered search terms literal instead of regular expressions.
    if role:
        df = df[df["Job_Role"].str.contains(role, case=False, na=False, regex=False)]
    if location:
        df = df[df["Location"].str.contains(location, case=False, na=False, regex=False)]
    if company:
        df = df[df["Company"].str.contains(company, case=False, na=False, regex=False)]
    return df


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/health")
def health():
    try:
        df = load_data()
        return jsonify({"status": "ok", "dataset_loaded": True, "records": int(len(df))})
    except (OSError, ValueError, pd.errors.ParserError) as exc:
        app.logger.exception("Health check failed while loading dataset")
        return jsonify({"status": "error", "dataset_loaded": False, "message": str(exc)}), 500


@app.get("/api/overview")
def overview():
    df = load_data()
    return jsonify({
        "total_jobs": int(len(df)),
        "total_roles": int(df["Job_Role"].nunique()),
        "total_companies": int(df["Company"].nunique()),
        "total_locations": int(df["Location"].nunique()),
    })


@app.get("/api/skills")
def skills():
    return jsonify(extract_skills(load_data()))


@app.get("/api/roles")
def roles():
    return jsonify(count_values(load_data()["Job_Role"], 10))


@app.get("/api/companies")
def companies():
    return jsonify(count_values(load_data()["Company"], 10))


@app.get("/api/locations")
def locations():
    values = []
    for value in load_data()["Location"]:
        values.extend(item.strip() for item in value.split(",") if item.strip())
    return jsonify(pd.Series(values, dtype="string").value_counts().head(10).to_dict())


@app.get("/api/experience")
def experience():
    return jsonify(extract_experience(load_data()))


@app.get("/api/options")
def options():
    df = load_data()
    return jsonify({
        "roles": sorted(df["Job_Role"].dropna().unique().tolist(), key=str.casefold),
        "companies": sorted(df["Company"].dropna().unique().tolist(), key=str.casefold),
        "locations": location_tokens(df),
    })


@app.get("/api/jobs")
def jobs():
    df = filter_jobs(
        load_data(),
        role=request.args.get("role", "").strip()[:120],
        location=request.args.get("location", "").strip()[:120],
        company=request.args.get("company", "").strip()[:120],
    )
    total = int(len(df))

    try:
        page = max(1, int(request.args.get("page", "1")))
        per_page = min(100, max(1, int(request.args.get("per_page", "25"))))
    except ValueError:
        return jsonify({"error": "page and per_page must be integers"}), 400

    start = (page - 1) * per_page
    records = df.iloc[start:start + per_page].to_dict(orient="records")
    return jsonify({
        "total": total,
        "page": page,
        "per_page": per_page,
        "pages": (total + per_page - 1) // per_page,
        "jobs": records,
    })


@app.get("/api/salary")
def salary():
    return jsonify({
        "available": False,
        "message": "Salary information is not present in the supplied dataset. Salary analysis requires a verified dataset containing salary values.",
    })


@app.errorhandler(404)
def not_found(_error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "API endpoint not found"}), 404
    return "Page not found", 404


@app.errorhandler(500)
def internal_error(error):
    app.logger.error("Unhandled application error: %s", error)
    if request.path.startswith("/api/"):
        return jsonify({"error": "An internal server error occurred. Check the deployment logs."}), 500
    return "An internal server error occurred. Please check the deployment logs.", 500


if __name__ == "__main__":
    # Debug mode is opt-in for local development only. Gunicorn is used in production.
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=debug)
