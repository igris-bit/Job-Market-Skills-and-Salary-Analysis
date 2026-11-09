# Job Market Skills & Salary Analysis

[![Live Deployment](https://img.shields.io/badge/Render-Live%20Demo-brightgreen?style=for-the-badge&logo=render)](https://job-market-skills-and-salary-analysis.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.14-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask%203.x-lightgrey?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Data%20Engine-Pandas%202.x-150458?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/Academic-B.Tech%20IIOT%20Project-orange?style=for-the-badge)](#team-members--git-branch-roster)

> **B.Tech Computer Science & Engineering (2nd Year) — IIOT / PBL Project**  
> **Center for Skill and Entrepreneurship Development (CSED)**  
> **Faculty Mentor:** Mr. Unwan Sir  

---

## 🌐 Live Deployed Application

> ### 🔗 **[ACCESS THE LIVE DEPLOYED DASHBOARD HERE](https://job-market-skills-and-salary-analysis.onrender.com/)**
> **Production URL:** `https://job-market-skills-and-salary-analysis.onrender.com/`  
> *(Hosted on Render with automatic HTTPS, Gunicorn WSGI, and in-memory LRU caching)*

---

## 📌 Project Overview & Problem Statement

In the modern technology job market, students and early-career developers face significant friction in identifying which technical competencies and programming frameworks genuinely align with hiring requirements. Traditional career guidance frequently relies on subjective advice, informal social media polls, or outdated academic syllabi.

**Job Market Skills and Salary Analysis** provides an empirical, data-backed solution through **Data-Driven Career Intelligence**. By aggregating and analyzing **12,000 real job postings** from Naukri across India, our application extracts actionable market signals regarding:
- Most frequently demanded programming languages and technical tools.
- Geographic distribution of career opportunities across major Indian metropolitan tech hubs.
- Industry-standard experience requirements across technical role families.
- Honest, transparent reporting of employment attributes and salary disclosure realities.

---

## 💡 Main USP: Data-Driven Career Intelligence

```
+-----------------------------------------------------------------------------------+
|                         DATA-DRIVEN CAREER INTELLIGENCE                           |
+-----------------------------------------------------------------------------------+
          |                               |                               |
          v                               v                               v
[ Empirical Evidence ]       [ Heuristic Standardization ]   [ Salary Honesty Policy ]
Statistical ranking of       Transforms noisy aliases        Transparent reporting that
12,000 job listings to       (e.g., 'py' -> Python,          salary data is unadvertised;
guide student learning.      'Bangalore' -> Bengaluru).      zero hallucination or fake ML.
```

1. **Evidence-Based Learning Roadmap**: Direct empirical validation of skill demand (Python, SQL, Machine Learning, AWS, Excel, Power BI).
2. **Transparent Skill & Location Normalization**: Resolves spelling variations, abbreviations, and composite city names without losing original source context.
3. **Conservative 18-Tier Role Taxonomy**: Heuristically maps complex, vendor-specific job titles into standard industry role categories (e.g., *Data Engineer*, *Data Scientist*, *Machine Learning Engineer*).
4. **Anti-Hallucination Data Ethics**: Explicitly reports that salary information is omitted in the source dataset rather than fabricating synthetic salary estimates.

---

## 👥 Team Members & Git Branch Roster

Every member of our 14-student project team collaborated via dedicated GitHub feature branches:

| S.No. | Student Name | Student ID | Git Branch | Core Role & Key Contributions |
|:---:|:---|:---:|:---:|:---|
| **1** | **Harshita Upadhyay** | **BCS2025411** | `Harshita` *(TL)* | **Team Leader & Project Architect**: Overall coordination, Git merge management, repo organization, and project delivery. |
| **2** | **Lokesh Shukla** | **BCS2025401** | `Lokesh` | **Backend Core Developer**: Flask API routes, error handlers, and server setup. |
| **3** | **Sudhanshu Singh** | **BCS2025402** | `Sudhanshu` | **USP Research & Documentation**: Formulated project USP (*Data-Driven Career Intelligence*) and value proposition. |
| **4** | **Rishabh Gupta** | **BCS2025406** | `Rishabh` | **Dataset Engineering Lead**: Schema specifications, column definitions, and data documentation. |
| **5** | **Anurag Verma** | **BCS2025409** | `Anurag` | **Data Preprocessing Specialist**: Regex pattern design, text sanitation, and whitespace normalization. |
| **6** | **Zainul Ali** | **BCS2025413** | `Zainul` | **Frontend UI & Styling Lead**: Modern CSS Grid/Flexbox architecture, hero banner styling, and card aesthetics. |
| **7** | **Ayushi** | **BCS2025414** | `Ayushi` | **Frontend DOM & State Integration**: Asynchronous API data binding, ranked lists rendering, and empty states. |
| **8** | **Nilansh Gupta** | **BCS2025416** | `Nilansh` | **Deployment & Performance Engineer**: Render cloud deployment, Gunicorn configuration, LRU caching, and data quality audit. |
| **9** | **Pranay Kesarwani** | **BCS2025417** | `Pranay` | **Directory Architecture Lead**: Module boundaries, folder structure design, and file hierarchy documentation. |
| **10** | **Mohammad Muneer** | **BCS2025418** | `Muneer` | **Experience & Statistical Analytics**: Extraction and computation of minimum/maximum work experience ranges. |
| **11** | **Kavyansh Bhadri** | **BCS2025419** | `Kavyansh` | **Entity Extraction & City Mapping**: Multi-city comma splitting, location frequency ranking, and regional filtering. |
| **12** | **Abhay** | **BCS2025421** | `Abhay` | **Fullstack Feature Engineer**: Integration of dynamic frontend search filters with backend API parameters. |
| **13** | **Sarvesh Singh** | **BCS2025422** | `Sarvesh` | **QA & Technical Governance**: Code quality validation, edge-case testing, and technical documentation. |
| **14** | **Sachin** | **BCS2025424** | `Sachin` | **Salary Analysis & Ethical Boundaries**: Salary coverage audit, missing-value disclosure reporting, and data ethics. |

---

## 🛠️ Technology Stack

| Layer | Technologies Used | Purpose |
|:---|:---|:---|
| **Backend Framework** | Python 3.10+, Flask 3.x, Flask-CORS | Lightweight REST API server & routing |
| **Data Engine** | Pandas 2.x, NumPy, Regular Expressions (`re`) | 12,000-record dataset filtering, aggregation, and caching |
| **Frontend UI** | Semantic HTML5, Modern CSS3 (Grid & Flexbox), Vanilla JS (ES6+) | Fast, responsive single-page dashboard with zero heavy bundle overhead |
| **Typography & Design** | DM Sans, Manrope, SVG UI Badges | Clean, readable visual hierarchy |
| **Caching & Performance** | `functools.lru_cache` | In-memory dataset caching (<15ms API response latency) |
| **WSGI & Server** | Gunicorn 22.x | High-concurrency production Python HTTP server |
| **Cloud Hosting** | Render Cloud Platform | Continuous deployment from GitHub with automated health monitoring |

---

## 📂 Repository Folder Structure

```
Job-Market-Skills-and-Salary-Analysis/
│
├── app.py                                      # Production Flask backend with caching & REST routes
├── naukri_data_science_jobs_india.csv          # 12,000 Indian tech job listings dataset
├── requirements.txt                            # Pinned Python package dependencies
├── Procfile                                    # Render WSGI deployment command (gunicorn app:app)
├── render.yaml                                 # Render Infrastructure as Code blueprint
├── .gitignore                                  # Git ignore rules for virtual environments & system files
├── README.md                                   # Project documentation and live link
├── DATA_QUALITY_AUDIT.md                       # Comprehensive data cleaning and validation audit
│
├── templates/
│   └── index.html                              # Clean, accessible dashboard interface
│
├── static/
│   ├── css/
│   │   └── style.css                           # Modern typography, responsive cards, and layout styles
│   └── js/
│       └── script.js                           # Asynchronous fetch client, pagination, and filter logic
│
├── docs/
│   ├── folder_structure.md                     # Detailed folder structure and governance guide
│   ├── tech_stack.md                           # Tech stack architecture and rationale
│   ├── usp_analysis.md                         # Detailed project USP and competitive advantage analysis
│   ├── dataset_description.md                  # Dataset schema, features, and cleaning pipeline
│   ├── api_documentation.md                    # REST API specifications and JSON samples
│   └── team_contributions.md                   # 14-member roster, student IDs, and branch mappings
│
├── reports/
│   ├── PROJECT_REPORT.md                       # Academic B.Tech project report (CSED / IIOT format)
│   └── Job_Market_Skills_and_Salary_Analysis_Report.pdf  # Downloadable submission-ready PDF report
│
├── presentation/
│   ├── PRESENTATION_SLIDES.md                  # 15-slide academic viva presentation script
│   ├── presentation.html                       # Browser-based interactive presentation deck
│   └── Job_Market_Skills_and_Salary_Analysis_Presentation.pptx  # Microsoft PowerPoint (.pptx) deck
│
└── reference and content/                      # University course templates, registers, and draft files
    ├── IIOT Project Report Format.pdf          # Official report formatting guidelines
    ├── IOT _ PBL Projects- Complete details.xlsx # Department project registration sheet
    ├── Job_Market_Skills_and_Salary_Analysis_Report.docx # Draft report
    └── USP_Analysis.md                         # Initial USP notes
```

---

## ⚡ Quick Start: Run Locally

### Prerequisites
- Python 3.10 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/upadhyayharshita07-cmd/Job-Market-Skills-and-Salary-Analysis.git
cd Job-Market-Skills-and-Salary-Analysis
```

### 2. Setup Virtual Environment

**Windows PowerShell:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```
Open your browser and navigate to: **`http://127.0.0.1:5000`**

---

## 🚀 Deployment on Render

The repository is pre-configured for automated continuous deployment on Render:

1. **Repository Connection**: Connect GitHub repository to Render as a **Web Service**.
2. **Environment**: Python 3.
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `gunicorn app:app`
5. **Health Check Path**: `/api/health`

The application configuration is also declared in `render.yaml` for instant Blueprint deployments.

---

## 🔌 REST API Endpoints

| Route | Method | Purpose |
|:---|:---:|:---|
| `/api/health` | `GET` | Health check and dataset verification |
| `/api/overview` | `GET` | Aggregate counts (listings, roles, companies, cities) |
| `/api/skills` | `GET` | Top 15 ranked skills |
| `/api/roles` | `GET` | Top 12 standardized role families |
| `/api/companies` | `GET` | Top 10 hiring companies |
| `/api/locations` | `GET` | Top 10 normalized cities |
| `/api/experience` | `GET` | Average min/max experience requirements |
| `/api/options` | `GET` | Search dropdown values for roles, cities, and companies |
| `/api/jobs` | `GET` | Filtered, grouped, and paginated job cards |
| `/api/salary` | `GET` | Salary data transparency disclosure |

---

## ⚖️ Ethical Considerations & Transparency

- **Data Integrity**: All statistics are directly derived from the 12,000 records in `naukri_data_science_jobs_india.csv`.
- **Missing Salary Disclosure**: The dataset contains no disclosed salary field. In alignment with academic rigor and data science ethics, the system reports salary data as missing rather than synthesizing misleading predictions.

---

## 🎓 Academic Submission Details

- **Academic Year**: 2026–2027
- **Institution**: Center for Skill and Entrepreneurship Development (CSED)
- **Department**: Department of Computer Science & Engineering
- **Program Code**: DA-021 (Career & Labour Market Analytics)
- **Team Leader**: Harshita Upadhyay (Student ID: `BCS2025411`)
- **Live URL**: [https://job-market-skills-and-salary-analysis.onrender.com/](https://job-market-skills-and-salary-analysis.onrender.com/)
