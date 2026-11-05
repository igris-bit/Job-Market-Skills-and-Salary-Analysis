from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pandas as pd
import re
import os

app = Flask(__name__)
CORS(app)

# ---------------- DATASET ----------------

DATASET_PATH = "naukri_data_science_jobs_india.csv"

EXPECTED_COLUMNS = [
    "Job_Role",
    "Company",
    "Location",
    "Job Experience",
    "Skills/Description"
]


# ---------------- LOAD DATA ----------------

def load_data():

    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError("Dataset CSV not found")

    df = pd.read_csv(DATASET_PATH)
    missing = [
        col for col in EXPECTED_COLUMNS
        if col not in df.columns
    ]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = df[EXPECTED_COLUMNS].copy()

    # data cleaning 

    for col in EXPECTED_COLUMNS:
        df[col] = df[col].fillna("").astype(str).str.strip()

    df = df[
        (df["Job_Role"] != "") &
        (df["Company"] != "")
    ]

    df = df.drop_duplicates()

    return df.reset_index(drop=True)


# ---------------- DATA PROCESSING ----------------

def extract_skills(df):

    skills = []

    for value in df["Skills/Description"]:

        for skill in value.split(","):

            skill = skill.strip().lower()

            if skill and skill not in ["skills", "it skills"]:
                skills.append(skill)

    return (
        pd.Series(skills)
        .value_counts()
        .head(15)
        .to_dict()
    )


def extract_experience(df):

    values = []

    for value in df["Job Experience"]:

        match = re.match(
            r"^\s*(\d+)\s*-\s*(\d+)\s*$",
            value
        )

        if match:
            minimum = int(match.group(1))
            maximum = int(match.group(2))

            if minimum <= maximum:
                values.append({
                    "minimum": minimum,
                    "maximum": maximum
                })

    if not values:
        return {
            "valid_records": 0,
            "average_minimum": None,
            "average_maximum": None
        }

    return {
        "valid_records": len(values),
        "average_minimum": round(
            sum(x["minimum"] for x in values) / len(values), 2
        ),
        "average_maximum": round(
            sum(x["maximum"] for x in values) / len(values), 2
        )
    }


def get_top_locations(df):

    locations = []

    for value in df["Location"]:

        for location in value.split(","):

            location = location.strip()

            if location:
                locations.append(location)

    return (
        pd.Series(locations)
        .value_counts()
        .head(10)
        .to_dict()
    )


# ---------------- API: OVERVIEW ----------------

@app.route("/api/overview", methods=["GET"])
def overview():

    df = load_data()

    return jsonify({
        "total_jobs": len(df),
        "total_roles": int(df["Job_Role"].nunique()),
        "total_companies": int(df["Company"].nunique()),
        "total_locations": int(df["Location"].nunique())
    })


# ---------------- API: SKILLS ----------------

@app.route("/api/skills", methods=["GET"])
def skills():

    df = load_data()

    return jsonify(extract_skills(df))


# ---------------- API: JOB ROLES ----------------

@app.route("/api/roles", methods=["GET"])
def roles():

    df = load_data()

    result = (
        df["Job_Role"]
        .value_counts()
        .head(10)
        .to_dict()
    )

    return jsonify(result)


# ---------------- API: COMPANIES ----------------

@app.route("/api/companies", methods=["GET"])
def companies():

    df = load_data()

    result = (
        df["Company"]
        .value_counts()
        .head(10)
        .to_dict()
    )

    return jsonify(result)


# ---------------- API: LOCATIONS ----------------

@app.route("/api/locations", methods=["GET"])
def locations():

    df = load_data()

    return jsonify(get_top_locations(df))


# ---------------- API: EXPERIENCE ----------------

@app.route("/api/experience", methods=["GET"])
def experience():

    df = load_data()

    return jsonify(extract_experience(df))


# ---------------- API: FILTER JOBS ----------------

@app.route("/api/jobs", methods=["GET"])
def jobs():

    df = load_data()

    role = request.args.get("role")
    location = request.args.get("location")
    company = request.args.get("company")

    if role:
        df = df[
            df["Job_Role"].str.contains(
                role, case=False, na=False
            )
        ]

    if location:
        df = df[
            df["Location"].str.contains(
                location, case=False, na=False
            )
        ]

    if company:
        df = df[
            df["Company"].str.contains(
                company, case=False, na=False
            )
        ]

    return jsonify({
        "total": len(df),
        "jobs": df.head(100).to_dict(orient="records")
    })


# ---------------- API: SALARY STATUS ----------------

@app.route("/api/salary", methods=["GET"])
def salary():

    return jsonify({
        "available": False,
        "message": (
            "Salary information is not present "
            "in the supplied dataset."
        )
    })
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- RUN SERVER ----------------

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )