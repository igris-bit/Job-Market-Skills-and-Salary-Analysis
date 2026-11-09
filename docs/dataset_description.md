# Dataset Description & Data Hygiene Audit

## 1. Dataset Overview

The project analyzes the primary dataset file: `naukri_data_science_jobs_india.csv`.

- **File Name**: `naukri_data_science_jobs_india.csv`
- **Total Records (Rows)**: 12,000 job advertisements
- **Columns (Features)**: 5 core attributes
- **Target Geographic Market**: India (Technology, Data Science, and Analytics sectors)
- **Collection Medium**: Web scraping / Public job aggregation from Naukri.com

---

## 2. Schema Definition

| Column Header | Data Type | Description | Sample Values | Preprocessing Transformations |
|:---|:---|:---|:---|:---|
| `Job_Role` | String | Advertised job title | `"Data Scientist"`, `"Lead Data Engineer"`, `"Senior ML Specialist"` | Unicode NFC normalization, trimming, keyword-based role family mapping into 18 categories. |
| `Company` | String | Hiring organization name | `"Accenture"`, `"Amazon"`, `"Tata Consultancy Services"`, `"Cognizant"` | Trimming, whitespace deduplication, case-insensitive indexation. |
| `Location` | String | Geographical work location(s) | `"Bangalore/Bengaluru"`, `"Hyderabad/Secunderabad"`, `"Pune(Hinjewadi)"` | Splitting comma-separated multi-cities; alias mapping (e.g., Bangalore → Bengaluru); region clustering (Delhi NCR). |
| `Job Experience` | String | Required experience range | `"3-8 Yrs"`, `"0-2 Yrs"`, `"5-10 Yrs"` | Regex extraction of lower/upper bounds (`(\d+)\s*-\s*(\d+)`); average calculations. |
| `Skills/Description` | String | Required technical skills & requirements | `"Python, SQL, AWS, Tableau, Machine Learning"` | Comma separation, lowercase normalization, alias grouping (e.g., `"py"` → `"Python"`), noise exclusion (`"skills"`). |

---

## 3. Data Cleaning & Transformation Pipeline

```
Raw CSV (12,000 Rows)
         |
         v
[ Deduplication & Validation ] -> Check required columns & strip whitespace
         |
         v
[ Text Sanitization ] ----------> Normalize Unicode characters via NFKC
         |
         v
[ Entity Normalization ] ------->
         ├── Locations: Split multi-cities & resolve aliases (Bangalore -> Bengaluru)
         ├── Job Roles: Classify into 18 deterministic role families (Data Engineer, ML Engineer...)
         └── Skills: Split comma list, map aliases (SQL, AWS, Python), filter generic tokens
         |
         v
[ LRU Memory Caching ] ---------> Cached in RAM for sub-15ms REST query execution
```

---

## 4. Key Quantitative Audit Findings

- **Total Job Postings**: 12,000
- **Distinct Raw Job Titles**: 6,563 (reduced to 18 standardized role families)
- **Distinct Companies**: 3,507 unique organizations
- **Top 5 Employment Hubs**:
  1. **Bengaluru**: 5,093 mentions
  2. **Pune**: 2,014 mentions
  3. **Hyderabad**: 1,940 mentions
  4. **Mumbai**: 1,452 mentions
  5. **Chennai**: 1,293 mentions
- **Top 5 In-Demand Skills**:
  1. **Python**
  2. **SQL**
  3. **Machine Learning**
  4. **AWS (Amazon Web Services)**
  5. **Excel / Power BI**
- **Experience Demand**:
  - Valid Range Records: >10,000 postings
  - Average Minimum Experience: ~2.8 years
  - Average Maximum Experience: ~6.4 years

---

## 5. Ethical Scope & Boundary Conditions

1. **Descriptive, Not Exhaustive**: The dataset reflects advertisements posted on a single portal during a specific snapshot; it does not capture the entirety of offline hiring, referrals, or government postings.
2. **Missing Salary Data**: The dataset lacks disclosed numerical compensation. Rather than predicting unverified figures, the project demonstrates academic honesty by explicitly declaring salary data as unavailable.

