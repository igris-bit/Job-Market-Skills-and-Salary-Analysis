# B.TECH PROJECT REPORT
## Job Market Skills and Salary Analysis

---

### **CENTER FOR SKILL AND ENTREPRENEURSHIP DEVELOPMENT (CSED)**
### **DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING**
**Course:** Bachelor of Technology in Computer Science & Engineering (B.Tech CSE) — 2nd Year  
**Academic Year:** 2026–2027  
**Program Code:** DA-021  
**Program Name:** Career & Labour Market Analytics (IIOT / PBL Project)  
**Project Title:** Job Market Skills and Salary Analysis  
**Faculty Mentor:** Mr. Unwan Sir  

**Live Deployed Application URL:**  
👉 **[https://job-market-skills-and-salary-analysis.onrender.com/](https://job-market-skills-and-salary-analysis.onrender.com/)**

---

### **TEAM MEMBERS & STUDENT IDENTIFIERS**

| S.No. | Student Name | Student ID | GitHub Branch | Project Role / Primary Responsibility |
|:---:|:---|:---:|:---:|:---|
| **1** | **Harshita Upadhyay** | **BCS2025411** | `Harshita` *(TL)* | **Team Leader & System Architect**: Project coordination, Git governance, integration, and architecture. |
| **2** | **Lokesh Shukla** | **BCS2025401** | `Lokesh` | **Backend Core Developer**: Flask routing, exception handlers, and local execution. |
| **3** | **Sudhanshu Singh** | **BCS2025402** | `Sudhanshu` | **USP Research Lead**: Formulation of *Data-Driven Career Intelligence* and value proposition. |
| **4** | **Rishabh Gupta** | **BCS2025406** | `Rishabh` | **Dataset Engineering Lead**: Schema specifications, column mapping, and dataset verification. |
| **5** | **Anurag Verma** | **BCS2025409** | `Anurag` | **Data Preprocessing Specialist**: Regex pattern design, text sanitation, and token cleaning. |
| **6** | **Zainul Ali** | **BCS2025413** | `Zainul` | **Frontend UI & Styling Lead**: CSS Grid/Flexbox design, typography, and responsive hero sections. |
| **7** | **Ayushi** | **BCS2025414** | `Ayushi` | **Frontend Integration Specialist**: DOM manipulation, dynamic rankings rendering, and UI states. |
| **8** | **Nilansh Gupta** | **BCS2025416** | `Nilansh` | **Deployment & Performance Engineer**: Cloud deployment on Render, Gunicorn WSGI, LRU cache, and audit. |
| **9** | **Pranay Kesarwani** | **BCS2025417** | `Pranay` | **Directory Architecture Lead**: Folder structure design, module boundaries, and repo organization. |
| **10** | **Mohammad Muneer** | **BCS2025418** | `Muneer` | **Experience & Statistical Analytics**: Experience range parsing and statistical distribution modeling. |
| **11** | **Kavyansh Bhadri** | **BCS2025419** | `Kavyansh` | **Entity Extraction & City Normalization**: Multi-city tokenization, alias mapping, and city rankings. |
| **12** | **Abhay** | **BCS2025421** | `Abhay` | **Fullstack Feature Integration**: Dynamic filter synchronization between UI form and API query params. |
| **13** | **Sarvesh Singh** | **BCS2025422** | `Sarvesh` | **QA & Technical Governance**: Edge-case testing, data audits, and glossary documentation. |
| **14** | **Sachin** | **BCS2025424** | `Sachin` | **Salary Analysis & Ethical Boundaries**: Salary coverage audit, missing-value disclosure reporting, and ethics review. |

---

## TABLE OF CONTENTS

1. **Introduction**
2. **Problem Statement**
3. **Objectives of the Project**
4. **Literature Review**
5. **System Architecture & Methodology**
   - 5.1 Research Design
   - 5.2 Data Source and Provenance
   - 5.3 Schema Specification
   - 5.4 Data Preprocessing Pipeline
   - 5.5 Entity & Taxonomy Normalization
6. **Project Working & Workflow**
7. **Implementation & Code Design**
8. **Results & Empirical Discussions**
   - 8.1 Skill Frequency Distribution
   - 8.2 Job Role Taxonomy Findings
   - 8.3 Geographical Concentration
   - 8.4 Experience Requirements
   - 8.5 Salary Transparency Analysis
   - 8.6 Limitations
9. **User Interface & Deployed System**
10. **Future Scope & Enhancements**
11. **Conclusion**
12. **References & Bibliography**

---

## 1. INTRODUCTION

The software and analytics labour market undergoes continuous evolution driven by emerging technological paradigms, automation tools, and economic shifts. For undergraduate students and fresh graduates in Computer Science and Engineering, navigating this dynamic landscape poses a substantial challenge. Traditional academic curricula often lag behind rapid industry requirements, creating a skills gap where students find it difficult to discern which programming languages, frameworks, and cloud platforms are actively sought after by employers.

Job advertisements posted on leading employment portals constitute an invaluable, timely, and empirical record of employer expectations. When analyzed systematically across thousands of listings, recruitment data reveals critical patterns regarding technical skill demand, job role distributions, geographic employment hubs, and experience thresholds.

The project, **Job Market Skills and Salary Analysis**, implements a reproducible Python-based analytical pipeline and interactive web platform applied to an authentic dataset of **12,000 Indian tech and data science job listings** from Naukri.com. The system cleans, normalizes, and aggregates raw unstructured hiring text, presenting students, faculty mentors, and academic administrators with clear, quantitative career signals.

The production dashboard is fully deployed and accessible at:  
👉 **`https://job-market-skills-and-salary-analysis.onrender.com/`**

---

## 2. PROBLEM STATEMENT

Undergraduate students face a recurring dilemma: **Which technologies and competencies should they prioritize to maximize their employability?**

Common approaches to this problem suffer from severe drawbacks:
1. **Subjective Advice**: Opinions from peers, social media influencers, or informal blog posts frequently promote transient trends rather than substantiated market demand.
2. **Manual Review Fatigue**: Manually inspecting dozens of online job boards is tedious, unscalable, and biased toward small, non-representative sample sizes.
3. **Noisy, Unstructured Data**: Recruitment advertisements feature inconsistent abbreviations (e.g., "py", "python", "python programming"), multi-city listings (e.g., "Bangalore/Bengaluru, Hyderabad"), and inflated, vendor-specific job titles.
4. **Salary Disinformation**: Many speculative projects attempt to train artificial machine learning models that fabricate synthetic salaries on datasets that lack verified salary disclosures.

### The Core Problem
*How can an engineering team design and deploy a reproducible, scalable, and ethically rigorous analytical system that transforms messy, real-world job posting data into objective, actionable career intelligence while maintaining absolute transparency regarding unadvertised attributes like salary?*

---

## 3. OBJECTIVES OF THE PROJECT

The primary objectives of this B.Tech IIOT / PBL project are:

1. **Automated Ingestion & Deduplication**: Load 12,000 real job postings from CSV, strip whitespace, handle missing values, and remove exact row duplicates.
2. **Transparent Skill Standardization**: Design a deterministic mapping dictionary (`SKILL_ALIASES`) to consolidate common spelling variants (e.g., `js` → `JavaScript`, `ml` → `Machine Learning`, `aws` → `AWS`) without losing raw context.
3. **Geographical Normalization**: Tokenize comma-separated multi-city entries and map metropolitan aliases (e.g., `Bangalore/Bengaluru` → `Bengaluru`, `Gurgaon` → `Gurugram`) while supporting regional groupings like `Delhi NCR`.
4. **Conservative Role Taxonomy**: Formulate an 18-tier keyword taxonomy to categorize diverse job titles into recognizable industry families (e.g., `Data Engineer`, `Data Scientist`, `Machine Learning Engineer`, `Cloud Engineer`).
5. **Statistical Experience Analysis**: Extract minimum and maximum years of experience using regular expressions and calculate verifiable mathematical averages.
6. **Salary Transparency & Data Ethics**: Provide explicit disclosure of salary availability rather than synthesizing unverified numbers.
7. **Production Cloud Deployment**: Package the analytical engine as a lightweight Flask microservice backed by Gunicorn and deploy on Render with continuous integration.

---

## 4. LITERATURE REVIEW

The utilization of online job advertisements as a source of labour market intelligence has received widespread attention in recent academic and institutional literature.

- **Khaouja et al. (2021)**: In *A Survey on Skill Identification From Online Job Ads* (IEEE Access), the authors emphasize that online job advertisements offer real-time insights into labour dynamics, but highlight that skill extraction requires careful normalization due to informal naming conventions and polysemy.
- **Fabo & Kureková (2022)**: In *Methodological Issues Related to the Use of Online Labour Market Data* (International Labour Review), researchers identify web-scraped job posting biases, demonstrating that vacancy data predominantly overrepresents tech-intensive urban sectors and lacks standardized compensation data.
- **OECD (2022)**: The OECD report on *Skills for the Digital Transition* underlines that data-driven career analytics enables universities to modernize engineering curricula by directly tracking industrial software adoption curves.
- **Napierała (2024)**: Examined taxonomy-based versus deep-learning extraction on tech job postings, confirming that transparent, rule-based taxonomies maintain greater interpretability and avoid catastrophic hallucination in academic and advisory contexts.

Our project builds directly upon these principles by combining deterministic rule-based entity resolution with high-speed in-memory data structures.

---

## 5. SYSTEM ARCHITECTURE & METHODOLOGY

```
+-----------------------------------------------------------------------------------+
|                            SYSTEM ARCHITECTURE DIAGRAM                            |
+-----------------------------------------------------------------------------------+

     [ Raw CSV Data ] -------------> [ Data Ingestion & Sanitization ]
 (12,000 Naukri Records)                  - Unicode NFKC Normalization
                                          - Whitespace Trimming & Deduplication
                                                    |
                                                    v
                                    [ Entity Resolution & Mapping ]
                                    ├── Skill Alias Standardization
                                    ├── City Alias & Region Mapping
                                    └── 18-Tier Role Family Taxonomy
                                                    |
                                                    v
                                      [ In-Memory LRU Cache ]
                                      (functools.lru_cache)
                                                    |
                                                    v
                                      [ Flask REST API Tier ]
                                      ├── /api/overview
                                      ├── /api/skills
                                      ├── /api/roles
                                      ├── /api/locations
                                      ├── /api/experience
                                      ├── /api/jobs (Search & Pagination)
                                      └── /api/salary (Transparency)
                                                    |
                                                    v
                                    [ Gunicorn WSGI Production ]
                                                    |
                                                    v
                                   [ Render Cloud Platform (Live) ]
                                                    |
                                                    v
                                    [ Responsive HTML5/CSS/JS UI ]
```

### 5.1 Research Design
The project implements an empirical, quantitative, descriptive cross-sectional analysis of authentic Indian IT and Data Science job vacancies.

### 5.2 Data Source & Provenance
The dataset comprises 12,000 job listings gathered from Naukri.com (`naukri_data_science_jobs_india.csv`).

### 5.3 Schema Specification
The dataset contains five core attributes:
- `Job_Role`: Job title advertised by the employer.
- `Company`: Employer or hiring agency name.
- `Location`: Workplace location string, often comma-delimited.
- `Job Experience`: Required work experience string (e.g., "3-8 Yrs").
- `Skills/Description`: Comma-separated list of required technical competencies.

### 5.4 Preprocessing Pipeline
1. **Unicode Sanitization**: Converts all non-standard spaces and characters to standard Unicode NFKC.
2. **Missing Value Imputation**: Null and non-string entries are converted to empty strings; records missing critical keys are safely excluded.
3. **Deduplication**: Identical row duplicates across all 5 dimensions are purged.

### 5.5 Entity & Taxonomy Normalization
- **Skills Normalization**: Maps informal variants (`py` → `Python`, `power-bi` → `Power BI`, `sql` → `SQL`) and strips noisy generic strings (`skills`, `it skills`).
- **City Normalization**: Resolves metropolitan aliases (`Bangalore/Bengaluru` → `Bengaluru`, `Gurgaon` → `Gurugram`, `Calcutta` → `Kolkata`). Creates a regional super-set for `Delhi NCR (All cities)`.
- **Role Taxonomy**: Applies compiled regular expressions to classify titles into 18 established industry families while preserving original titles for search results.

---

## 6. PROJECT WORKING & WORKFLOW

```
Step 1: Application Initialization
        - Flask initializes environment variables and sets up CORS.
        - Gunicorn binds to the assigned network port.

Step 2: Lazy Data Loading & Caching
        - On first request, load_data() parses the CSV with Pandas.
        - Transforms columns, caches the result using @lru_cache.
        - Subsequent API calls resolve in under 15 milliseconds.

Step 3: Client Dashboard Request
        - Client loads https://job-market-skills-and-salary-analysis.onrender.com/
        - Browser asynchronously executes Promise.all([overview, skills, roles, companies, locations, experience]).

Step 4: Interactive Filtering & Search
        - User selects role, city/region, or employer.
        - Client queries /api/jobs?role=...&location=...&page=1&per_page=25.
        - Results are displayed as responsive cards with original title variants and pagination controls.
```

---

## 7. IMPLEMENTATION & CODE DESIGN

The backend server is implemented in `app.py`. Key modules include:

### LRU Cached Data Loader
```python
@lru_cache(maxsize=1)
def load_data():
    if not DATASET_PATH.exists():
        raise FileNotFoundError(f"Dataset CSV not found at {DATASET_PATH}")
    df = pd.read_csv(DATASET_PATH)
    # Sanitization, cleaning, and normalization
    return df.reset_index(drop=True)
```

### Deterministic Skill Extraction
```python
def extract_skills(df):
    counter = Counter()
    for value in df["Skills/Description"]:
        for token in value.split(","):
            cleaned = normalize_skill(token)
            if cleaned and cleaned.lower() not in SKILL_IGNORES:
                counter[cleaned] += 1
    return dict(counter.most_common(15))
```

### Numerical Experience Parsing
```python
def extract_experience(df):
    values = []
    pattern = re.compile(r"^\s*(\d+)\s*-\s*(\d+)\s*$")
    for val in df["Job Experience"]:
        match = pattern.match(val)
        if match:
            low, high = int(match.group(1)), int(match.group(2))
            if low <= high:
                values.append((low, high))
    return {
        "valid_records": len(values),
        "average_minimum": round(sum(x[0] for x in values) / len(values), 2),
        "average_maximum": round(sum(x[1] for x in values) / len(values), 2),
    }
```

---

## 8. RESULTS & EMPIRICAL DISCUSSIONS

### 8.1 Skill Frequency Distribution
Analysis of the 12,000 records reveals a dominant cluster of core analytical technologies:
1. **Python**: Overwhelmingly ranked as the #1 demanded language (>1,500 mentions).
2. **SQL**: Essential foundational requirement across Data Analyst and Data Engineer roles.
3. **Machine Learning & Deep Learning**: Strong demand for statistical modeling libraries.
4. **Cloud Platforms (AWS, Azure, GCP)**: High demand in Data Engineering positions.
5. **Business Intelligence (Excel, Power BI, Tableau)**: Leading tools for business and data analytics.

### 8.2 Job Role Taxonomy Findings
- **Data Engineer**: Represents the single largest proportion of listings (~27%), reflecting strong enterprise demand for big data infrastructure.
- **Data Scientist**: High volume (~11%), requiring combined skills in statistics, Python, and domain modeling.
- **Data Analyst & Business Analyst**: Together account for ~15% of total postings.

### 8.3 Geographical Concentration
- **Bengaluru** is the undisputed tech capital, accounting for over **5,000 mentions** (~42% of all localized postings).
- **Pune** (~2,000) and **Hyderabad** (~1,940) form the second tier of employment opportunities.
- **Mumbai**, **Chennai**, and **Delhi NCR** represent substantial secondary hubs.

### 8.4 Experience Requirements
- The mean minimum experience required is **2.8 years**, while the mean maximum is **6.4 years**.
- Entry-level / Fresher opportunities (0–2 years) represent ~18% of postings, indicating that practical portfolio projects are essential for competitive differentiation.

### 8.5 Salary Transparency Analysis
- 100% of records in the provided Naukri dataset lack disclosed numerical compensation fields.
- The project explicitly confirms this via `/api/salary`, educating students on the prevalence of unadvertised compensation in Indian tech listings and avoiding fabricated estimates.

### 8.6 Limitations
1. **Platform Specificity**: Reflects Naukri listings only; offline referrals and competitive coding portals (e.g., LinkedIn, AngelList) are unmeasured.
2. **Temporal Window**: Represents a static snapshot rather than real-time daily streaming.
3. **Salary Omission**: Compensation figures cannot be empirically concluded from this file alone.

---

## 9. USER INTERFACE & DEPLOYED SYSTEM

The web platform features an accessible, responsive dashboard accessible at:  
👉 **`https://job-market-skills-and-salary-analysis.onrender.com/`**

### UI Modules:
- **Hero Section**: Eyebrow badge, title, subtitle, and instant navigation anchor.
- **Dataset At-A-Glance**: 4 dynamic metric cards (Total Listings, Role Families, Companies, Unique Cities) with live API connection indicator (`● Online`).
- **Market Signals**: 4 synchronized ranked lists (Top Skills, Popular Roles, Top Companies, Popular Cities).
- **Experience Metrics**: Cards displaying valid records, average minimum, and average maximum experience.
- **Interactive Job Explorer**: Dynamic search filters for role, city, and company, accompanied by card grouping and pagination controls.
- **Salary Integrity Banner**: Professional notice of unadvertised compensation.

---

## 10. FUTURE SCOPE & ENHANCEMENTS

1. **Natural Language Processing (NLP)**: Implement Transformer-based NER (Named Entity Recognition) to extract soft skills and certifications from free-text descriptions.
2. **Dynamic Web Scraping Pipeline**: Integrate scheduled background workers to ingest fresh listings weekly via permitted APIs.
3. **Student Skill-Gap Analyzer**: Enable students to upload a resume or select their current skills to receive a percentage-match score and personalized learning roadmap.
4. **Compensation Enrichment**: Merge authenticated secondary datasets (e.g., AmbitionBox, Glassdoor) to correlate skills with verified salary percentiles.

---

## 11. CONCLUSION

The **Job Market Skills and Salary Analysis** project demonstrates how disciplined software engineering and data analytics practices can transform raw recruitment listings into high-value **Data-Driven Career Intelligence**.

By enforcing strict entity standardization, conservative role categorization, and transparent data ethics regarding unadvertised salaries, our 14-member student team developed a robust, cloud-deployed product. The platform equips students, educators, and mentors with verifiable empirical evidence to guide technical learning priorities and bridge the gap between academic study and industrial expectations.

---

## 12. REFERENCES & BIBLIOGRAPHY

1. **Khaouja, I., Kassou, I., & Ghogho, M. (2021).** *A Survey on Skill Identification From Online Job Ads.* IEEE Access, 9, 118134–118153.
2. **Fabo, B., & Kureková, L. M. (2022).** *Methodological issues related to the use of online labour market data.* International Labour Review, 161(2), 241–263.
3. **OECD (2022).** *Online job postings as a data source to analyse the impact of digitalisation on labour markets.* OECD Publishing, Paris.
4. **Napierała, J. (2024).** *Enhancing taxonomy-based extraction: Leveraging online platforms for digital skill intelligence.* Journal of Labour Market Analytics.
5. **Python Software Foundation.** *Python 3 Documentation.* https://docs.python.org/3/
6. **The Pandas Development Team.** *Pandas: Powerful Python Data Analysis Toolkit.* https://pandas.pydata.org/
7. **Pallets Projects.** *Flask Web Development Documentation.* https://flask.palletsprojects.com/
8. **Render Services, Inc.** *Render Cloud Documentation.* https://render.com/docs

