# REST API Documentation

The backend exposes a lightweight, performant REST API powering the interactive dashboard. All endpoints return data in standard `application/json` format.

**Base URL**: `https://job-market-skills-and-salary-analysis.onrender.com`  
**Local URL**: `http://127.0.0.1:5000`

---

## Endpoint Summary

| HTTP Method | Route | Description |
|:---|:---|:---|
| `GET` | `/` | Renders the HTML5 dashboard interface (`index.html`) |
| `GET` | `/api/health` | Health check route verifying dataset load status and record count |
| `GET` | `/api/overview` | Returns aggregate metrics: total jobs, roles, companies, and cities |
| `GET` | `/api/skills` | Returns top 15 most frequent skills after alias standardization |
| `GET` | `/api/roles` | Returns top 12 standardized job role families |
| `GET` | `/api/companies` | Returns top 10 companies with the highest hiring volume |
| `GET` | `/api/locations` | Returns top 10 normalized cities by listing frequency |
| `GET` | `/api/experience` | Computes statistical metrics on required experience levels |
| `GET` | `/api/options` | Returns distinct options for populating search filter dropdowns |
| `GET` | `/api/jobs` | Filtered, grouped, and paginated job listing records |
| `GET` | `/api/salary` | Reports salary transparency status and data availability disclaimer |

---

## Detailed Endpoint Reference

### 1. Health Check
- **Route**: `GET /api/health`
- **Response**:
```json
{
  "status": "ok",
  "dataset_loaded": true,
  "records": 12000
}
```

### 2. Overview Statistics
- **Route**: `GET /api/overview`
- **Response**:
```json
{
  "total_jobs": 12000,
  "total_roles": 19,
  "total_companies": 3507,
  "total_locations": 292,
  "total_regions": 2566
}
```

### 3. Top Skills
- **Route**: `GET /api/skills`
- **Response**:
```json
{
  "Python": 1582,
  "SQL": 1240,
  "Machine Learning": 985,
  "AWS": 745,
  "Excel": 620,
  "Power BI": 540,
  "Java": 490
}
```

### 4. Search & Filter Jobs (Paginated)
- **Route**: `GET /api/jobs`
- **Query Parameters**:
  - `role` *(string, optional)*: Filter by standardized role family (e.g. `Data Engineer`)
  - `location` *(string, optional)*: Filter by normalized city or region (e.g. `Bengaluru`, `Delhi NCR (All cities)`)
  - `company` *(string, optional)*: Case-insensitive substring match for employer
  - `page` *(integer, optional, default: 1)*: Target page number
  - `per_page` *(integer, optional, default: 25, max: 100)*: Items per page
- **Sample Request**:
  `GET /api/jobs?role=Data%20Engineer&location=Bengaluru&page=1&per_page=25`
- **Response**:
```json
{
  "total": 1420,
  "total_records": 1845,
  "page": 1,
  "per_page": 25,
  "pages": 57,
  "jobs": [
    {
      "Clean_Role": "Data Engineer",
      "Company": "Amazon",
      "Job Experience": "3-6 Yrs",
      "Job_Role": "Data Engineer II - Big Data Analytics",
      "Location": "Bengaluru",
      "Skills/Description": "Python, Spark, AWS, Redshift, SQL",
      "records_in_group": 3,
      "source_titles": [
        "Data Engineer II - Big Data Analytics",
        "Data Engineer - AWS Ecosystem"
      ]
    }
  ]
}
```

### 5. Salary Status Disclaimer
- **Route**: `GET /api/salary`
- **Response**:
```json
{
  "available": false,
  "message": "Salary data is not included in this dataset. No salary estimates are generated."
}
```

