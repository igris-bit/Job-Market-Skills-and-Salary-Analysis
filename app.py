from functools import lru_cache
from pathlib import Path
import os
import re
import unicodedata

import pandas as pd
from flask import Flask, jsonify, render_template, request

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "naukri_data_science_jobs_india.csv"
EXPECTED_COLUMNS = ["Job_Role", "Company", "Location", "Job Experience", "Skills/Description"]

SKILL_ALIASES = {
    "python programming": "Python", "py": "Python", "python": "Python",
    "js": "JavaScript", "javascript": "JavaScript",
    "ml": "Machine Learning", "machine-learning": "Machine Learning",
    "machine learning": "Machine Learning", "deep-learning": "Deep Learning",
    "deep learning": "Deep Learning", "powerbi": "Power BI", "power-bi": "Power BI",
    "power bi": "Power BI", "ms excel": "Excel", "excel": "Excel",
    "structured query language": "SQL", "sql": "SQL",
    "amazon web services": "AWS", "google cloud platform": "Google Cloud",
    "gcp": "Google Cloud", "google cloud": "Google Cloud",
}
SKILL_IGNORES = {"skills", "it skills", "skill", "technical skills", ""}

# Canonical city aliases. Delhi NCR is a region; constituent cities remain selectable.
LOCATION_ALIASES = {
    "bangalore": "Bengaluru", "bengaluru": "Bengaluru",
    "bangalore/bengaluru": "Bengaluru", "bengaluru/bangalore": "Bengaluru",
    "hyderabad": "Hyderabad", "secunderabad": "Hyderabad",
    "hyderabad/secunderabad": "Hyderabad", "secunderabad/hyderabad": "Hyderabad",
    "gurgaon": "Gurugram", "gurugram": "Gurugram",
    "gurgaon/gurugram": "Gurugram", "gurugram/gurgaon": "Gurugram",
    "delhi": "Delhi", "new delhi": "Delhi", "dehli": "Delhi", "new dehli": "Delhi",
    "delhi/ncr": "Delhi", "delhi / ncr": "Delhi", "delhi ncr": "Delhi",
    "delhi/n.c.r.": "Delhi", "delh ncr": "Delhi", "delhi /ncr": "Delhi",
    "delhi n.c.r": "Delhi", "delhi ncr (all cities)": "Delhi",
    "noida": "Noida", "greater noida": "Greater Noida",
    "mumbai (all areas)": "Mumbai", "mumbai": "Mumbai",
    "pune (all areas)": "Pune", "pune": "Pune",
    "chennai": "Chennai", "kolkata": "Kolkata", "calcutta": "Kolkata",
    "ahmedabad": "Ahmedabad", "kochi": "Kochi", "cochin": "Kochi",
    "gurugram (all areas)": "Gurugram",
}
DELHI_NCR_CITIES = {"Delhi", "Gurugram", "Noida", "Greater Noida"}
REGION_LABEL = "Delhi NCR (All cities)"

# Deliberately conservative role families. Original titles are always retained.
ROLE_PATTERNS = [
    ("Machine Learning Engineer", r"\b(machine learning|ml engineer|deep learning|nlp engineer)\b"),
    ("Data Scientist", r"\b(data scientist|applied scientist|decision scientist)\b"),
    ("Data Engineer", r"\b(data engineer|big data engineer|data engineering)\b"),
    ("Data Analyst", r"\b(data analyst|analytics analyst|data analytics)\b"),
    ("Business Analyst", r"\b(business analyst|business analysis)\b"),
    ("Data Architect", r"\b(data architect|data architecture)\b"),
    ("Data Science / Analytics", r"\b(data science|analytics)\b"),
    ("Database Engineer / Administrator", r"\b(database|dba|database administrator)\b"),
    ("Software Engineer / Developer", r"\b(software engineer|software developer|application developer)\b"),
    ("Python Developer", r"\bpython developer\b"),
    ("Java Developer", r"\bjava developer\b"),
    ("Cloud Engineer", r"\b(cloud engineer|aws engineer|azure engineer|devops engineer)\b"),
    ("Product Analyst / Manager", r"\b(product analyst|product manager)\b"),
    ("Research Analyst", r"\bresearch analyst\b"),
    ("Reporting / BI Analyst", r"\b(bi analyst|business intelligence|power bi|tableau)\b"),
    ("QA / Test Engineer", r"\b(qa engineer|test engineer|testing)\b"),
    ("Technical Lead", r"\b(technical lead|tech lead)\b"),
    ("Other Analyst", r"\banalyst\b"),
]

app = Flask(__name__)


def _clean_text(value):
    value = unicodedata.normalize("NFKC", str(value or ""))
    return re.sub(r"\s+", " ", value).strip()


def normalize_location(value):
    raw = _clean_text(value)
    # Ignore locality annotations such as (Cyber City) or (Sector-125 Noida)
    # so the dropdown contains one city-level choice instead of many variants.
    raw = re.sub(r"\s*\([^)]*\)", "", raw).strip(" ,")
    key = raw.casefold().replace("–", "-")
    key = re.sub(r"\s*/\s*", "/", key)
    key = re.sub(r"\s+", " ", key)
    if key in LOCATION_ALIASES:
        return LOCATION_ALIASES[key]
    # Retain unknown locations rather than silently merging them.
    return raw.title()


def split_locations(value):
    # Commas separate locations. Known slash-pairs are aliases and stay together.
    return [normalize_location(part) for part in _clean_text(value).split(",") if _clean_text(part)]


def normalize_job_role(value):
    original = _clean_text(value)
    if not original:
        return "Unclassified"

    # Remove obvious ad copy and compensation/eligibility fragments for classification only.
    text = original.casefold()
    text = re.sub(r"\b\d+(?:\.\d+)?\s*(?:lpa|lakhs?|per annum)\b", " ", text)
    text = re.sub(r"\b(fresher|can apply|cab|urgent hiring|immediate joiner|walk-in)\b", " ", text)
    text = re.sub(r"\s+", " ", text)

    for canonical, pattern in ROLE_PATTERNS:
        if re.search(pattern, text, flags=re.I):
            return canonical
    # Keep unfamiliar/noisy titles out of the filter taxonomy; the original title remains visible per listing.
    return "Other / Unclassified"


def normalize_company(value):
    value = _clean_text(value)
    return value


@lru_cache(maxsize=1)
def load_data():
    """Load once per worker, validate source columns, and derive clean analytical fields."""
    if not DATASET_PATH.is_file():
        raise FileNotFoundError(f"Dataset not found: {DATASET_PATH.name}")
    df = pd.read_csv(DATASET_PATH, low_memory=False)
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing)}")

    df = df[EXPECTED_COLUMNS].copy()
    for column in EXPECTED_COLUMNS:
        df[column] = df[column].fillna("").map(_clean_text)

    df = df[(df["Job_Role"] != "") & (df["Company"] != "")]
    df = df.drop_duplicates().reset_index(drop=True)

    df["Clean_Role"] = df["Job_Role"].map(normalize_job_role)
    df["Group_Role"] = df.apply(
        lambda row: row["Job_Role"] if row["Clean_Role"] in {"Other Analyst", "Other / Unclassified"}
        else row["Clean_Role"], axis=1
    )
    # Collapse company-name case/spacing variants while retaining the most common
    # original spelling as the dropdown label (e.g. ACME, Acme, acme -> Acme).
    company_labels = {}
    for key, group in df.groupby(df["Company"].map(lambda x: normalize_company(x).casefold())):
        counts = group["Company"].value_counts()
        company_labels[key] = sorted(counts.items(), key=lambda item: (-item[1], item[0].casefold()))[0][0]
    df["Clean_Company"] = df["Company"].map(lambda x: company_labels[normalize_company(x).casefold()])
    df["City_List"] = df["Location"].map(split_locations)
    df["Clean_Location"] = df["City_List"].map(lambda xs: ", ".join(dict.fromkeys(xs)))
    df["Region_List"] = df["City_List"].map(
        lambda xs: ["Delhi NCR"] if any(x in DELHI_NCR_CITIES for x in xs) else []
    )
    return df


def ranked_counts(values, limit=10):
    series = pd.Series(list(values), dtype="string")
    series = series[series.notna() & series.str.strip().ne("")]
    counts = series.value_counts()
    # Explicit stable count-descending ordering; ties alphabetically.
    ordered = sorted(counts.items(), key=lambda item: (-int(item[1]), str(item[0]).casefold()))
    return {str(k): int(v) for k, v in ordered[:limit]}


def extract_skills(df, limit=15):
    found = []
    for description in df["Skills/Description"]:
        for raw in description.split(","):
            key = re.sub(r"\s+", " ", raw).strip().casefold()
            if key in SKILL_IGNORES:
                continue
            canonical = SKILL_ALIASES.get(key, _clean_text(raw).title())
            if canonical and canonical.casefold() not in SKILL_IGNORES:
                found.append(canonical)
    return ranked_counts(found, limit)


def extract_experience(df):
    ranges = []
    for value in df["Job Experience"]:
        match = re.fullmatch(r"(\d+)\s*-\s*(\d+)", value)
        if match:
            low, high = map(int, match.groups())
            if low <= high:
                ranges.append((low, high))
    if not ranges:
        return {"valid_records": 0, "average_minimum": None, "average_maximum": None}
    return {
        "valid_records": len(ranges),
        "average_minimum": round(sum(x[0] for x in ranges) / len(ranges), 2),
        "average_maximum": round(sum(x[1] for x in ranges) / len(ranges), 2),
    }


def all_city_tokens(df):
    return [city for cities in df["City_List"] for city in cities]


def filter_jobs(df, role="", location="", company=""):
    if role:
        df = df[df["Clean_Role"].str.casefold() == role.casefold()]
    if location:
        if location == REGION_LABEL:
            df = df[df["City_List"].map(lambda xs: any(x in DELHI_NCR_CITIES for x in xs))]
        else:
            df = df[df["City_List"].map(lambda xs: location in xs)]
    if company:
        df = df[df["Clean_Company"].str.contains(company, case=False, na=False, regex=False)]
    return df


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/health")
def health():
    try:
        df = load_data()
        return jsonify({"status": "ok", "dataset_loaded": True, "records": int(len(df))})
    except Exception:
        app.logger.exception("Health check failed")
        return jsonify({"status": "error", "dataset_loaded": False, "message": "Dataset could not be loaded."}), 500


@app.get("/api/overview")
def overview():
    df = load_data()
    cities = set(all_city_tokens(df))
    return jsonify({
        "total_jobs": int(len(df)),
        "total_roles": int(df["Clean_Role"].nunique()),
        "total_companies": int(df["Clean_Company"].nunique()),
        "total_locations": len(cities),
        "total_regions": int(sum(bool(x) for x in df["Region_List"])),
    })


@app.get("/api/skills")
def skills():
    return jsonify(extract_skills(load_data()))


@app.get("/api/roles")
def roles():
    return jsonify(ranked_counts(load_data()["Clean_Role"], 12))


@app.get("/api/companies")
def companies():
    return jsonify(ranked_counts(load_data()["Clean_Company"], 10))


@app.get("/api/locations")
def locations():
    return jsonify(ranked_counts(all_city_tokens(load_data()), 10))


@app.get("/api/experience")
def experience():
    return jsonify(extract_experience(load_data()))


@app.get("/api/options")
def options():
    df = load_data()
    cities = sorted(set(all_city_tokens(df)), key=str.casefold)
    locations = [REGION_LABEL] + cities
    roles_list = sorted(df["Clean_Role"].dropna().unique().tolist(), key=str.casefold)
    companies_list = sorted(df["Clean_Company"].dropna().unique().tolist(), key=str.casefold)
    return jsonify({"roles": roles_list, "companies": companies_list, "locations": locations})


@app.get("/api/jobs")
def jobs():
    try:
        page = max(1, int(request.args.get("page", "1")))
        per_page = min(100, max(1, int(request.args.get("per_page", "25"))))
    except ValueError:
        return jsonify({"error": "page and per_page must be integers"}), 400

    df = filter_jobs(
        load_data(),
        role=request.args.get("role", "").strip()[:120],
        location=request.args.get("location", "").strip()[:120],
        company=request.args.get("company", "").strip()[:120],
    )
    total_records = int(len(df))
    group_columns = ["Group_Role", "Clean_Company", "Clean_Location", "Job Experience"]
    grouped = (
        df.groupby(group_columns, dropna=False, sort=False)
        .agg(
            Clean_Role=("Clean_Role", "first"),
            Job_Role=("Job_Role", "first"),
            Company=("Clean_Company", "first"),
            Location=("Clean_Location", "first"),
            Skills_Description=("Skills/Description", "first"),
            records_in_group=("Job_Role", "size"),
            source_titles=("Job_Role", lambda values: list(pd.unique(values))[:5]),
        )
        .reset_index()
        .rename(columns={"Skills_Description": "Skills/Description"})
        .sort_values(["records_in_group", "Clean_Role"], ascending=[False, True], kind="stable")
    )
    total_groups = int(len(grouped))
    pages = (total_groups + per_page - 1) // per_page
    start = (page - 1) * per_page
    records = grouped.iloc[start:start + per_page].drop(columns=["Group_Role"]).to_dict(orient="records")
    return jsonify({
        "total": total_groups,
        "total_records": total_records,
        "page": page,
        "per_page": per_page,
        "pages": pages,
        "jobs": records,
    })


@app.get("/api/salary")
def salary():
    return jsonify({
        "available": False,
        "message": "Salary data is not included in this dataset. No salary estimates are generated.",
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
        return jsonify({"error": "Internal server error. Check application logs."}), 500
    return "Internal server error.", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")),
            debug=os.environ.get("FLASK_DEBUG") == "1")
