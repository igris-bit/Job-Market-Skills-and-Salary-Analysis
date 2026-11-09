# Project Folder Structure & Architecture

```
Job-Market-Skills-and-Salary-Analysis/
│
├── .gitignore                                  # Git ignore rules for virtual environments, caches, and system files
├── Procfile                                    # Render deployment web process definition (Gunicorn WSGI)
├── render.yaml                                 # Render infrastructure as code (Blueprint configuration)
├── requirements.txt                            # Pinned Python package dependencies for production
├── README.md                                   # Primary project documentation with live link and team roster
├── DATA_QUALITY_AUDIT.md                       # Comprehensive data cleaning and validation audit
├── app.py                                      # Main Flask application with caching, taxonomy mapping, & REST APIs
├── naukri_data_science_jobs_india.csv          # Source dataset: 12,000 Indian Data Science job postings
│
├── templates/                                  # Server-side HTML templates (Jinja2)
│   └── index.html                              # Responsive single-page dashboard UI
│
├── static/                                     # Static web assets served to clients
│   ├── css/
│   │   └── style.css                           # Modern typography, card layouts, badges, and responsive design
│   └── js/
│       └── script.js                           # Asynchronous API fetcher, pagination, and filter state manager
│
├── docs/                                       # In-depth architectural, technical, and process documentation
│   ├── folder_structure.md                     # Directory hierarchy guide and repository layout (this file)
│   ├── tech_stack.md                           # Tech stack overview, library breakdown, and architectural rationale
│   ├── usp_analysis.md                         # Main USP: Data-Driven Career Intelligence & competitive advantages
│   ├── dataset_description.md                  # Dataset schema, field definitions, data hygiene, and constraints
│   ├── api_documentation.md                    # REST API endpoint reference, parameters, and sample JSON payloads
│   └── team_contributions.md                   # 14-member student roster, branch mapping, and role distribution
│
├── reports/                                    # Academic project reports for university submission
│   ├── PROJECT_REPORT.md                       # Complete academic B.Tech IIOT / PBL report (Markdown edition)
│   └── Job_Market_Skills_and_Salary_Analysis_Report.pdf  # Formatted, submission-ready PDF report
│
├── presentation/                               # Viva / evaluation presentation materials
│   ├── PRESENTATION_SLIDES.md                  # Comprehensive 15-slide academic slide deck with speaker notes
│   ├── presentation.html                       # Standalone browser-based interactive presentation deck
│   └── Job_Market_Skills_and_Salary_Analysis_Presentation.pptx  # Microsoft PowerPoint (.pptx) presentation
│
└── reference and content/                      # Historical course guidelines, raw documents, and university templates
    ├── IIOT Project Report Format.pdf          # Official department report guidelines
    ├── IOT _ PBL Projects- Complete details.xlsx # Departmental PBL project registration sheet
    ├── Job_Market_Skills_and_Salary_Analysis_Report.docx # Preliminary draft document
    ├── USP_Analysis.docx                       # Initial USP document draft
    └── USP_Analysis.md                         # Markdown summary of project USP
```

---

## Directory Roles & Guidelines

| Directory / File | Description | Maintainer / Responsibility |
|:---|:---|:---|
| `app.py` | Core backend engine: data loading with LRU cache, city normalization, regex-based role taxonomy, search grouping, and JSON API routes. | Team Leader & Backend Leads |
| `naukri_data_science_jobs_india.csv` | Immutable primary dataset containing 12,000 real job postings across India. | Data Engineering Team |
| `templates/` & `static/` | Web presentation tier built with semantic HTML5, CSS Grid/Flexbox, and vanilla ES6 JavaScript. | Frontend Development Team |
| `docs/` | Technical, architecture, and team governance documentation for open-source and evaluator review. | Documentation Team |
| `reports/` | Formal academic project documentation aligned with university B.Tech curriculum and IIOT/PBL standards. | Research & Report Leads |
| `presentation/` | Evaluation presentation deck in Markdown, interactive HTML, and PowerPoint formats for viva voce. | Team Leader & Presenters |
| `reference and content/` | Archive of university-supplied rubrics, Excel registers, and historical drafts. | Archival Reference |

