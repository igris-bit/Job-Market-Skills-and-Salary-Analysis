# Presentation Slide Deck
## Job Market Skills and Salary Analysis

**Academic Track:** B.Tech Computer Science & Engineering (2nd Year) — IIOT / PBL Project  
**Center:** Center for Skill and Entrepreneurship Development (CSED)  
**Program Code:** DA-021 (Career & Labour Market Analytics)  
**Mentor:** Mr. Unwan Sir  
**Live Deployed Application:** [https://job-market-skills-and-salary-analysis.onrender.com/](https://job-market-skills-and-salary-analysis.onrender.com/)

---

## Slide 1: Title & Project Overview

### Slide Content:
- **Project Title:** Job Market Skills and Salary Analysis
- **Sub-heading:** Transforming 12,000 Indian Tech Job Postings into Data-Driven Career Intelligence
- **Course & Institution:** B.Tech Computer Science & Engineering (2nd Year), CSED
- **Faculty Mentor:** Mr. Unwan Sir
- **Team Leaders:** Harshita Upadhyay (`BCS2025411`) & Zainul Ali (`BCS2025413`)
- **Live Demo:** `https://job-market-skills-and-salary-analysis.onrender.com/`

> **Speaker Notes:**  
> *"Good morning respected faculty members and examiners. Today, our 14-member engineering team is presenting 'Job Market Skills and Salary Analysis', our B.Tech second-year IIOT project under the guidance of Mr. Unwan Sir. The project tackles the disconnect between academic learning and industry expectations by analyzing 12,000 live Indian tech job postings to provide actionable career intelligence. The application is fully built, tested, and deployed live on Render."*

---

## Slide 2: The Core Problem

### Slide Content:
- **Curriculum Misalignment:** Students face uncertainty in identifying which programming tools and technologies employers actively require.
- **Subjective & Noisy Guidance:** Advice on social media or forums is subjective, unverified, and anecdotal.
- **Data Fragmentation:** Real-world recruitment listings contain noisy abbreviations, composite city names, and erratic job titles.
- **The "Fake Salary" Epidemic:** Many academic analytics projects attempt to fabricate or predict salaries on datasets where salary was never disclosed.

> **Speaker Notes:**  
> *"Every engineering undergraduate asks: 'What technologies should I focus on to become employable?' Relying on internet hearsay or outdated syllabi leads to wasted preparation time. Furthermore, recruitment data in India is messy and rarely includes published compensation. Our goal was to build a disciplined, reproducible engineering pipeline to replace guesswork with empirical evidence."*

---

## Slide 3: Main Project USP — Data-Driven Career Intelligence

### Slide Content:
- **Core Value:** Data-Driven Career Intelligence — empirical market validation replacing guesswork.
- **Four Fundamental Pillars:**
  1. **Empirical Evidence:** Frequency rankings across 12,000 postings guide high-ROI learning.
  2. **Heuristic Normalization:** Standardizes noisy variations (`py` → `Python`, `Bangalore` → `Bengaluru`).
  3. **Conservative Role Taxonomy:** 18 distinct role families preserve original titles while grouping cleanly.
  4. **Strict Data Ethics (Anti-Hallucination):** Transparently reports that salary data is unadvertised rather than training flawed synthetic ML models.

> **Speaker Notes:**  
> *"Our primary USP is Data-Driven Career Intelligence. We don't just dump charts; we normalize messy entities, categorize roles with a clear heuristic taxonomy, and maintain strict data ethics. When a dataset omits salary, we say so upfront, teaching responsible data science practices."*

---

## Slide 4: Project Team Roster (14 Members)

### Slide Content:
| S.No. | Student Name | Student ID | Branch | Key Contribution |
|:---:|:---|:---:|:---:|:---|
| **1** | **Harshita Upadhyay (TL)** | **BCS2025411** | `Harshita` | Team Leader, Integration & Architecture |
| **2** | **Lokesh Shukla** | **BCS2025401** | `Lokesh` | Backend Core & Flask API Routing |
| **3** | **Sudhanshu Singh** | **BCS2025402** | `Sudhanshu` | USP Formulation & Strategic Research |
| **4** | **Rishabh Gupta** | **BCS2025406** | `Rishabh` | Dataset Engineering & Schema Definition |
| **5** | **Anurag Verma** | **BCS2025409** | `Anurag` | Data Preprocessing & Text Sanitation |
| **6** | **Zainul Ali (TL)** | **BCS2025413** | `Zainul` | Team Leader & Frontend UI Architecture |
| **7** | **Ayushi** | **BCS2025414** | `Ayushi` | Frontend DOM Logic & Asynchronous State |
| **8** | **Nilansh Gupta** | **BCS2025416** | `Nilansh` | Cloud Deployment, WSGI & LRU Caching |
| **9** | **Pranay Kesarwani** | **BCS2025417** | `Pranay` | Directory Hierarchy & Repo Governance |
| **10** | **Mohammad Muneer** | **BCS2025418** | `Muneer` | Experience Analysis & Distribution Metrics |
| **11** | **Kavyansh Bhadri** | **BCS2025419** | `Kavyansh` | City Normalization & Multi-City Tokenization |
| **12** | **Abhay** | **BCS2025421** | `Abhay` | Fullstack Search Filter Integration |
| **13** | **Sarvesh Singh** | **BCS2025422** | `Sarvesh` | QA Testing & Technical Governance |
| **14** | **Sachin** | **BCS2025424** | `Sachin` | Salary Ethics Audit & Boundary Verification |

> **Speaker Notes:**  
> *"Our project was engineered collaboratively using individual Git feature branches for every team member. Harshita led the architectural governance, Lokesh and Nilansh engineered the backend and cloud deployment, Zainul and Ayushi designed the frontend, and our data specialists ensured rigorous cleaning and documentation."*

---

## Slide 5: System Architecture & Technology Stack

### Slide Content:
- **Presentation Tier:** Semantic HTML5, modern CSS Grid/Flexbox, Vanilla JavaScript ES6+ (Zero bloated bundlers, sub-second load times).
- **Application Tier:** Python 3.10+, Flask 3.x, Flask-CORS, Gunicorn WSGI HTTP Server.
- **Data Engine:** Pandas 2.x, Regular Expressions (`re`), `functools.lru_cache` (In-memory caching for <15ms latency).
- **Cloud Infrastructure:** Render Cloud Platform with automated build and deployment pipelines.

> **Speaker Notes:**  
> *"We avoided bloated frontend frameworks and heavy database engines. By combining Flask with an in-memory Pandas DataFrame cached via Python's LRU cache, our REST API resolves complex multi-filter queries in under 15 milliseconds."*

---

## Slide 6: Dataset Schema & Data Hygiene Pipeline

### Slide Content:
- **Source:** 12,000 real job postings from Naukri.com across Indian tech corridors.
- **Five Primary Dimensions:**
  1. `Job_Role`: Job title advertised.
  2. `Company`: Hiring employer.
  3. `Location`: Geographical workplace.
  4. `Job Experience`: Required experience range.
  5. `Skills/Description`: Technical skill keywords.
- **Cleaning Pipeline:** Unicode NFKC normalization, whitespace trimming, row deduplication, and case-folding.

> **Speaker Notes:**  
> *"Our dataset covers 12,000 verified tech listings. We developed an automated hygiene pipeline that normalizes Unicode characters, purges duplicate rows, and parses comma-separated entities cleanly."*

---

## Slide 7: Entity Resolution & Skill Standardization

### Slide Content:
- **The Challenge:** Inconsistent naming variations in recruitment advertisements.
- **Deterministic Mapping:**
  - `python programming`, `py` → **Python**
  - `js`, `javascript` → **JavaScript**
  - `ml`, `machine learning`, `deep-learning` → **Machine Learning / Deep Learning**
  - `aws`, `amazon web services` → **AWS**
  - `ms excel`, `excel` → **Excel**
- **Noise Elimination:** Discards generic placeholders like `"skills"` and `"it skills"`.

> **Speaker Notes:**  
> *"Rather than relying on black-box heuristics, we use transparent alias dictionaries to map spelling variations into canonical skill entities, ensuring our rankings reflect true employer intent."*

---

## Slide 8: Role Taxonomy & Geographical Normalization

### Slide Content:
- **18-Tier Conservative Role Taxonomy:**
  - Regex-based classification into *Data Engineer*, *Data Scientist*, *Data Analyst*, *Machine Learning Engineer*, *Cloud Engineer*, etc.
  - Original employer job titles are preserved and displayed on every result card.
- **Geographical Normalization:**
  - Multi-city listings split into individual tokens.
  - Aliases consolidated: `Bangalore/Bengaluru` → `Bengaluru`, `Gurgaon` → `Gurugram`.
  - Regional cluster support: `Delhi NCR (All cities)` aggregates Delhi, Gurugram, Noida, and Greater Noida.

> **Speaker Notes:**  
> *"We grouped thousands of arbitrary titles into 18 established industry families while preserving the employer's original listing title. We also resolved city aliases and enabled regional filtering for Delhi NCR."*

---

## Slide 9: Top Technical Skills in Demand

### Slide Content:
- **1. Python (Rank #1):** Dominant language (>1,500 mentions) — mandatory across ML, Data Engineering, and Data Science.
- **2. SQL (Rank #2):** Core requirement for relational querying and database manipulation.
- **3. Machine Learning (Rank #3):** High demand for predictive analytics and modeling.
- **4. AWS / Cloud Platforms:** Crucial for distributed data infrastructure and deployment.
- **5. Excel & Power BI:** Strong demand in business intelligence and reporting roles.

> **Speaker Notes:**  
> *"Our empirical analysis confirms that Python and SQL form the dual foundation of modern data careers. Cloud skills like AWS and visualization tools like Power BI are essential secondary competencies."*

---

## Slide 10: Role & Geographic Distribution

### Slide Content:
- **Role Breakdown:**
  - **Data Engineer:** ~27% of postings (Massive demand for big data pipelines).
  - **Data Scientist:** ~11% of postings (Focus on statistics and advanced modeling).
  - **Data Analyst / BI:** ~15% of postings (Reporting, dashboards, and KPI analysis).
- **Geographic Breakdown:**
  - **Bengaluru:** The tech powerhouse (>5,000 listings, ~42% of market).
  - **Tier-2 Hubs:** Pune (~2,000 listings) and Hyderabad (~1,940 listings).
  - **Northern / Coastal Hubs:** Mumbai, Chennai, and Delhi NCR represent key clusters.

> **Speaker Notes:**  
> *"Data Engineering actually exceeds pure Data Science in total hiring volume in India today, reflecting the industry's need for data infrastructure. Geographically, Bengaluru remains the undisputed technology capital."*

---

## Slide 11: Experience Requirements & Distribution

### Slide Content:
- **Statistical Findings:**
  - Valid Range Records: >10,000 listings.
  - **Average Minimum Experience:** 2.8 Years.
  - **Average Maximum Experience:** 6.4 Years.
- **Entry-Level Opportunities (0–2 Years):**
  - Account for approximately ~18% of available positions.
  - Implication: Fresh graduates must showcase hands-on capstone projects to overcome experience barriers.

> **Speaker Notes:**  
> *"With an average minimum requirement of nearly 3 years, fresh graduates face tough entry barriers. Our findings demonstrate that academic theory alone is insufficient; practical, deployed projects are critical to winning entry-level roles."*

---

## Slide 12: Salary Transparency & Data Ethics

### Slide Content:
- **The Finding:** 100% of records in the provided Naukri dataset omit disclosed salary figures.
- **Our Ethical Policy:**
  - We refuse to fabricate synthetic salaries or fit unverified regression models.
  - The dashboard explicitly informs users that compensation data is unadvertised.
- **Industry Insight:** In the Indian tech market, compensation is predominantly negotiated based on candidate pedigree rather than published in job postings.

> **Speaker Notes:**  
> *"A hallmark of our project is academic integrity. Many projects train flawed predictive models on missing data. We chose ethical honesty: our platform provides an explicit disclaimer and educates students on hiring realities."*

---

## Slide 13: Live Deployed System Walkthrough

### Slide Content:
- **Production URL:** `https://job-market-skills-and-salary-analysis.onrender.com/`
- **Interactive Capabilities:**
  - Live metric summary cards with `● Online` status.
  - Synchronized ranked frequency lists for Skills, Roles, Companies, and Cities.
  - Dynamic multi-parameter search filter (Role × Location × Company).
  - Client-side pagination with selectable page sizes (25, 50, 100).
  - Full mobile responsiveness across smartphones, tablets, and desktops.

> **Speaker Notes:**  
> *"Let us transition to the live system on Render. You can see our overview cards updating dynamically, our search filters responding instantly, and grouped cards presenting clean pagination."*

---

## Slide 14: Future Scope & Roadmap

### Slide Content:
- **NLP Semantic Extraction:** Deploy Transformer-based NER models on full job descriptions.
- **Student Skill-Gap Analyzer:** Upload resume text to receive an automated match score against target roles.
- **Continuous Ingestion Pipeline:** Automated weekly job scraping via authorized APIs.
- **Compensation Enrichment:** Integrate authenticated secondary salary benchmarks.

> **Speaker Notes:**  
> *"For future work, we plan to implement a resume skill-gap analyzer and deploy continuous scrapers to maintain a living, real-time pulse of the Indian technology market."*

---

## Slide 15: Conclusion & Q&A

### Slide Content:
- **Summary:** Successfully built, documented, and deployed an end-to-end Career Intelligence platform across 12,000 job listings.
- **Engineering Excellence:** Sub-15ms cached REST API, clean modular folder structure, and 14-member collaborative Git workflow.
- **Live URL:** [https://job-market-skills-and-salary-analysis.onrender.com/](https://job-market-skills-and-salary-analysis.onrender.com/)
- **Thank You!** We now invite questions from our faculty mentor and examiners.

> **Speaker Notes:**  
> *"In conclusion, 'Job Market Skills and Salary Analysis' turns chaotic hiring data into clear career signals for students. On behalf of all 14 team members and our mentor Mr. Unwan Sir, thank you for your time. We are now open for questions."*

