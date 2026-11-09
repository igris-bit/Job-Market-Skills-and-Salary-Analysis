# Technology Stack & Architectural Rationale

This document details the technologies, libraries, frameworks, and architectural principles utilized in the **Job Market Skills and Salary Analysis** project.

---

## 1. Architecture Overview

The application follows a **Decoupled Client-Server Architecture** optimized for high-performance exploratory data analysis and responsive user interaction.

```
+-------------------------------------------------------------+
|                     Client Browser Tier                     |
|  - Semantic HTML5 (Dashboard Structure)                    |
|  - Custom CSS3 (Flexbox, CSS Grid, DM Sans & Manrope)       |
|  - Vanilla JavaScript ES6+ (Fetch API, Client State)        |
+-------------------------------------------------------------+
                              |
                     HTTPS / JSON REST
                              |
+-------------------------------------------------------------+
|                      Application Tier                       |
|  - Python 3.10+ / Flask Framework                           |
|  - Flask-CORS (Cross-Origin Resource Sharing)               |
|  - Gunicorn WSGI Server (Green Unicorn Production Daemon)   |
|  - Python functools.lru_cache (In-Memory Dataset Cache)     |
+-------------------------------------------------------------+
                              |
                     Data Processing Tier
                              |
+-------------------------------------------------------------+
|                     Data & Analytics Engine                 |
|  - Pandas (High-speed tabular processing & aggregation)     |
|  - Regular Expressions (re) & Unicodedata Normalization     |
|  - 12,000-Record Naukri Job Postings Dataset (.csv)         |
+-------------------------------------------------------------+
                              |
                     Deployment Platform
                              |
+-------------------------------------------------------------+
|               Render Cloud Application Hosting              |
|  - Fully managed Linux container environment                |
|  - Continuous Deployment via GitHub Repository Webhook      |
|  - Auto-scaling & Health check monitoring (/api/health)     |
+-------------------------------------------------------------+
```

---

## 2. Technology Selection & Versions

### A. Backend & Data Processing
- **Python 3.10+ / 3.14**: Chosen for its robust data manipulation ecosystem, readability, and performance.
- **Flask (v3.0+)**: Lightweight, unopinionated microframework allowing rapid endpoint creation with minimal overhead, suitable for serving REST APIs and static dashboards.
- **Pandas (v2.0+)**: High-performance data structures (`DataFrame`, `Series`) providing vectorized aggregations, string manipulations, and deduplication across 12,000 records in sub-50ms execution times.
- **LRU Cache (`functools.lru_cache`)**: Caches the cleaned dataset in memory, preventing repeated disk reads and ensuring near-instantaneous API response times (<15ms).
- **Gunicorn (v22.0+)**: Enterprise-grade Python WSGI HTTP server designed for UNIX/Linux production environments on Render, utilizing pre-fork worker models to handle concurrent requests reliably.

### B. Frontend & UI
- **HTML5**: Semantic tags (`<header>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`) ensuring accessibility and clean document outline.
- **CSS3 (Modern Vanilla)**:
  - Responsive layouts using **CSS Grid** (`grid-template-columns: repeat(...)`) and **Flexbox**.
  - Modern typography pairing: **DM Sans** (body text) and **Manrope** (bold display headings).
  - Modern visual design: CSS custom properties (`--blue`, `--ink`, `--line`), smooth gradients, badge pills, and elevation shadows.
- **Vanilla JavaScript (ES6+)**:
  - `fetch()` API for asynchronous, non-blocking REST communication.
  - Client-side pagination state management (`page`, `pageSize`, `filters`).
  - Safe DOM generation via `document.createElement()` and `replaceChildren()` to eliminate XSS risks.
  - Number formatting using `Intl.NumberFormat` / `toLocaleString('en-IN')` for Indian numbering standards.

### C. Deployment & DevOps
- **Platform**: Render Cloud Hosting (`https://job-market-skills-and-salary-analysis.onrender.com/`).
- **Configuration**:
  - `Procfile`: Configured with `web: gunicorn app:app` for production WSGI serving.
  - `render.yaml`: Blueprint definition specifying environment, build command, run command, and `/api/health` monitoring.
- **Version Control**: Git & GitHub, utilizing feature branches for all 14 team members.

---

## 3. Comparative Justification: Why This Stack?

| Proposed Alternative | Chosen Solution | Technical Justification |
|:---|:---|:---|
| **Streamlit / Gradio** | **Flask + Custom Frontend** | Streamlit is heavy, reruns the entire Python script on every user interaction, and provides limited layout control. Flask provides production-grade REST APIs, decoupling the UI from data processing and enabling seamless web integration. |
| **Relational DB (PostgreSQL / MySQL)** | **In-Memory Pandas + CSV** | The dataset is static (12,000 records). Loading into memory via Pandas with `@lru_cache` eliminates database latency, database connection pooling issues, and hosting costs while executing complex regex filters in milliseconds. |
| **Heavy Frontend (React / Angular)** | **Vanilla ES6 JS** | For an exploratory analytics dashboard, React introduces bundlers (Webpack/Vite), node_modules bloat, and build-step latency. Vanilla JS delivers sub-second initial page loads and zero compile overhead. |

