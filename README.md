# Job Market Skills and Salary Analysis

A Flask + Pandas dashboard for exploring job listings: commonly mentioned skills, popular roles, companies, locations, experience ranges, and filtered job records.

> **Data limitation:** the included CSV does not contain salary values. The salary endpoint intentionally reports salary analysis as unavailable instead of estimating or fabricating salary figures.

## Features

- Dashboard overview for listing, role, company, and location counts
- Top skills, roles, companies, and locations
- Summary of valid job-experience ranges
- Search by role, location, and company
- Server-side pagination for search results
- Dataset validation, missing-value cleanup, and duplicate removal
- Dataset loaded once per worker and reused for requests
- Health endpoint for deployment checks
- Responsive HTML/CSS/JavaScript frontend

## Project structure

```text
.
├── app.py
├── naukri_data_science_jobs_india.csv
├── requirements.txt
├── Procfile
├── render.yaml
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    └── js/script.js
```

The `reference and content/` folder contains supporting academic/report files and is not required to run the web application.

## Run locally

Requires Python 3.10 or newer.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

If PowerShell blocks environment activation, you can run `.venv\Scripts\python.exe -m pip install -r requirements.txt` and `.venv\Scripts\python.exe app.py` instead.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python app.py
```

For local debugging only, set `FLASK_DEBUG=1`. Debug mode is off by default.

## API endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Dashboard |
| `/api/health` | Dataset and application health |
| `/api/overview` | Overall counts |
| `/api/skills` | Top 15 extracted skills |
| `/api/roles` | Top 10 job roles |
| `/api/companies` | Top 10 companies |
| `/api/locations` | Top 10 location tokens |
| `/api/experience` | Valid experience range summary |
| `/api/options` | Role, company, and location options for search |
| `/api/jobs` | Filtered job records with pagination |
| `/api/salary` | Explicit salary-data availability status |

Example search:

```text
/api/jobs?role=data%20scientist&location=Bangalore&page=1&per_page=25
```

`page` defaults to `1`; `per_page` defaults to `25` and is capped at `100`. Supported filters are `role`, `location`, and `company`. Search terms are treated as literal text, not regular expressions.

## Deploy to Render

1. Push the complete project to a GitHub repository.
2. In Render, choose **New + → Web Service** and connect the repository.
3. Use these settings:
   - **Runtime:** Python 3
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
   - **Root directory:** leave blank when `app.py`, `requirements.txt`, and the CSV are in the repository root.
4. Deploy and wait for the build to finish.
5. Visit `/api/health` on your deployed service. A healthy response includes `"status": "ok"` and the number of records loaded.
6. Open the root URL and test dashboard metrics, dropdowns, filtering, and pagination.

`render.yaml` is included as an optional Blueprint configuration. If using it, choose Render's Blueprint flow.

## Data quality notes

- The app verifies that the CSV contains the five required columns before processing it.
- Blank required job roles and company names are excluded; duplicate rows are removed.
- Skill names receive conservative whitespace cleanup and a small set of common alias normalizations. This does not replace a more rigorous taxonomy.
- Location counts are based on location strings/tokens in the dataset. City naming may vary between listings.
- Experience averages include only ranges written as `minimum-maximum` whole numbers.
- Findings describe this dataset and its collection scope. They should not be presented as a census of all jobs in India.

## Troubleshooting

- **Build fails:** inspect Render's build logs and confirm the CSV and `requirements.txt` are committed.
- **Application fails to start:** confirm the start command is `gunicorn app:app` and that `app.py` defines `app = Flask(__name__)`.
- **Health endpoint returns 500:** check that the CSV filename and required column names match exactly.
- **Dashboard data does not load:** open browser Developer Tools → Network and Console to check failed requests.
- **Large dataset changes:** redeploy after committing the updated CSV; each worker caches its own in-memory copy.

## License and source

Add the dataset's original source, collection date, and any applicable license/usage terms before publishing the project publicly. Do not claim a license unless you have confirmed it.
