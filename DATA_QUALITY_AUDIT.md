# Data quality audit

Audit performed against the supplied `naukri_data_science_jobs_india.csv` (12,000 rows, five columns).

## Source facts

- Rows: 12,000
- Columns: `Job_Role`, `Company`, `Location`, `Job Experience`, `Skills/Description`
- Exact duplicate rows across all five columns: 0
- Distinct raw job-title strings: 6,563
- Distinct raw location strings: 822
- Distinct company strings: 3,507
- Repeated `(Job_Role, Company, Location, Job Experience)` combinations: 598 combinations occur more than once. These are review candidates, not proven duplicate advertisements.

## Normalized location results

Splitting comma-separated locations and applying the documented city aliases yields 292 distinct city tokens. Top normalized city mentions:

| City | Mentions |
|---|---:|
| Bengaluru | 5,093 |
| Pune | 2,014 |
| Hyderabad | 1,940 |
| Mumbai | 1,452 |
| Chennai | 1,293 |
| Gurugram | 1,252 |
| Delhi | 780 |
| Noida | 534 |
| Kolkata | 290 |
| Ahmedabad | 217 |

A listing with multiple locations contributes one mention to each named city. The Delhi NCR regional filter is a union of Delhi, Gurugram, Noida and Greater Noida, so regional counts should not be added to city counts.

## Role taxonomy results

The deterministic title taxonomy maps titles into 19 role families, including `Other / Unclassified`. The original source title is retained on each result card. Current top normalized role families:

| Role family | Records |
|---|---:|
| Data Engineer | 3,271 |
| Other / Unclassified | 1,929 |
| Other Analyst | 1,822 |
| Data Scientist | 1,332 |
| Data Analyst | 1,099 |
| Business Analyst | 645 |

This is a transparent keyword heuristic, not a validated occupational classification model. Inspect and extend `ROLE_PATTERNS` before using the categories for high-stakes conclusions.

## Search-result grouping\n\nThe upgraded search groups records by standardized role family (with original titles kept separate for broad fallback categories), company, normalized city set and experience range. On this dataset, this produces 10,349 result groups representing 12,000 source records. Group cards show the number of source records represented and up to five original title variants. This is presentation-level grouping; it does not delete source rows.\n\n## Known limits

- The dataset contains no salary, stable job ID, posting date or original listing URL.
- Exact duplicates can be removed, but repeated combinations cannot safely be removed as duplicates.
- Location and job-title normalization are rule-based. Unknown locations are retained; unclassified titles are grouped rather than guessed.
- Counts describe this dataset only, not the full Indian job market.
