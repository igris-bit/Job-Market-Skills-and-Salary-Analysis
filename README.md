# Job Market Skills & Salary Analysis

A responsive Flask + Pandas dashboard for exploring skills, standardized job-role families, companies, locations and experience requirements in a 12,000-row Naukri job-listing dataset.

> **Salary limitation:** the supplied CSV has no salary field. The application explicitly reports salary analysis as unavailable and does not estimate or fabricate salary values.

## What's improved

- Frequency rankings are explicitly sorted by count, descending, with alphabetical tie-breaking.
- City aliases are normalized (for example Bangalore/Bengaluru → Bengaluru).
- Delhi NCR is available as a regional filter that includes Delhi, Gurugram, Noida and Greater Noida, while individual cities remain selectable.
- Job-role dropdowns use a conservative role-family taxonomy. Original job titles are preserved and shown on each listing.
- Unknown or noisy titles are grouped as `Other / Unclassified` instead of polluting the filter list.
- Search filters use searchable browser suggestions (datalist), so long lists are easier to navigate.
- Search supports pagination and page sizes of 25, 50 or 100.
- Empty, loading and error states are shown in the interface.
- Exact duplicate rows are removed. Search results group matching role-family/company/city/experience combinations into one card and show how many source records were grouped; they are not deleted from the dataset.

## Data-cleaning policy

### Locations

The app normalizes common aliases such as:

- Bangalore, Bengaluru, Bangalore/Bengaluru → Bengaluru
- Hyderabad, Hyderabad/Secunderabad → Hyderabad
- Gurgaon, Gurugram, Gurgaon/Gurugram → Gurugram
- New Delhi, Delhi / NCR, Delhi NCR and the observed typo DELH NCR → Delhi
- Mumbai (All Areas) → Mumbai

Delhi NCR is a region filter spanning Delhi, Gurugram, Noida and Greater Noida. It is not a replacement for the individual city values. Unknown location strings are retained rather than guessed.

### Job roles

The app classifies recognizable titles into broad role families (Data Engineer, Data Scientist, Data Analyst, Business Analyst, Software Engineer / Developer, etc.). The raw `Job_Role` field is retained. Titles that cannot be confidently classified are grouped under `Other / Unclassified` for filtering; the original title remains visible in search results.

This is a transparent heuristic taxonomy, not a machine-learning classifier. Review the patterns in `ROLE_PATTERNS` in `app.py` and extend them when new legitimate role families appear.

### Repeated job records

The dataset contains no stable job ID, posting date or source URL. Therefore identical title/company/location/experience combinations cannot be proven to be duplicate advertisements. Exact identical rows are removed. Search results visually group matching standardized role/company/city/experience combinations and show the number of source records represented. The underlying records remain in the CSV and are not deleted.

### Skills

Common spelling and abbreviation aliases are normalized. Generic labels such as `IT Skills` are excluded from the top-skill ranking. Skill extraction still depends on the source's comma-separated `Skills/Description` field.

## Project structure

```text
.
├── app.py
├── naukri_data_science_jobs_india.csv
├── requirements.txt
├── Procfile
├── render.yaml
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    └── js/script.js
```

## Run locally

Requires Python 3.10+.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

## API endpoints

| Endpoint | Description |
|---|---|
| `/` | Dashboard |
| `/api/health` | Dataset/application health |
| `/api/overview` | Total listings, role families, companies and normalized cities |
| `/api/skills` | Top 15 skills by frequency |
| `/api/roles` | Top standardized role families by frequency |
| `/api/companies` | Top 10 companies |
| `/api/locations` | Top 10 normalized cities |
| `/api/experience` | Valid experience range summary |
| `/api/options` | Search suggestions for roles, cities/regions and companies |
| `/api/jobs` | Grouped filtered listings with pagination |
| `/api/salary` | Explicit salary-data availability status |

Example:

```text
/api/jobs?role=Data%20Engineer&location=Bengaluru&page=1&per_page=25
```

Supported filters: `role`, `location`, `company`, `page`, `per_page`.

## Deploy to Render

The included `render.yaml` configures a Python web service.

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Health check path: `/api/health`

Connect the repository to Render as a Web Service or use the Blueprint flow for `render.yaml`. Ensure the CSV is committed at the repository root.

## Important interpretation notes

- Counts describe this 12,000-row supplied dataset, not all job openings in India.
- Location rankings count normalized city mentions. A listing naming multiple cities contributes to each named city.
- The Delhi NCR region filter can include one listing in multiple constituent city filters. Do not add regional and city counts together.
- Broad role-family counts are based on keyword rules and should be reviewed as the taxonomy evolves.
- The CSV has no salary field, job ID, posting date or listing URL. Salary trends and definitive advertisement-level deduplication are therefore not possible from this file alone.

## Dataset provenance

Before public submission, document the original dataset URL/source, date collected, and its applicable license or usage terms. Do not claim a license without verifying it.
