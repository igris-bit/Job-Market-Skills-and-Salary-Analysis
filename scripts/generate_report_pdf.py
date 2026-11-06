import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

os.makedirs('reports', exist_ok=True)
pdf_path = os.path.join('reports', 'Job_Market_Skills_and_Salary_Analysis_Report.pdf')

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    leftMargin=40,
    rightMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

primary_color = colors.HexColor('#173eaa')
secondary_color = colors.HexColor('#2457d6')
text_dark = colors.HexColor('#17243b')
accent_bg = colors.HexColor('#f0f5ff')
border_color = colors.HexColor('#dce7ff')

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=primary_color,
    alignment=1,
    spaceAfter=8
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=16,
    textColor=secondary_color,
    alignment=1,
    spaceAfter=15
)

meta_style = ParagraphStyle(
    'DocMeta',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=text_dark,
    alignment=1,
    spaceAfter=4
)

h1_style = ParagraphStyle(
    'H1',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=17,
    textColor=primary_color,
    spaceBefore=14,
    spaceAfter=6
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=text_dark,
    spaceAfter=5
)

callout_style = ParagraphStyle(
    'Callout',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#1e429d'),
    alignment=1
)

table_header_style = ParagraphStyle(
    'TableHeader',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8,
    leading=10,
    textColor=colors.white,
    alignment=1
)

table_cell_style = ParagraphStyle(
    'TableCell',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=7.5,
    leading=9.5,
    textColor=text_dark
)

table_cell_bold = ParagraphStyle(
    'TableCellBold',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=7.5,
    leading=9.5,
    textColor=text_dark
)

story = []

# Title & Institution
story.append(Paragraph('CENTER FOR SKILL AND ENTREPRENEURSHIP DEVELOPMENT (CSED)', meta_style))
story.append(Paragraph('DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING', meta_style))
story.append(Paragraph('B.Tech Computer Science &amp; Engineering — 2nd Year | Academic Year: 2026–2027', meta_style))
story.append(Spacer(1, 6))
story.append(HRFlowable(width='100%', thickness=2, color=primary_color, spaceBefore=2, spaceAfter=8))

story.append(Paragraph('JOB MARKET SKILLS AND SALARY ANALYSIS', title_style))
story.append(Paragraph('Career &amp; Labour Market Analytics (Program Code: DA-021)', subtitle_style))
story.append(Paragraph('<b>Faculty Mentor:</b> Mr. Unwan Sir', meta_style))
story.append(Spacer(1, 6))

# Callout Box for Live Deployed Link
deployed_text = '<b>Live Deployed Project Link (Accessible to Checker):</b><br/><font color="#2457d6"><u>https://job-market-skills-and-salary-analysis.onrender.com/</u></font>'
callout_data = [[Paragraph(deployed_text, callout_style)]]
callout_table = Table(callout_data, colWidths=[515])
callout_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), accent_bg),
    ('BOX', (0,0), (-1,-1), 1.5, secondary_color),
    ('PADDING', (0,0), (-1,-1), 7),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
]))
story.append(callout_table)
story.append(Spacer(1, 8))

# Team Roster Table
story.append(Paragraph('PROJECT TEAM ROSTER &amp; GIT BRANCH MAPPINGS', h1_style))
team_data = [
    [Paragraph('S.No.', table_header_style), Paragraph('Student Name', table_header_style), Paragraph('Student ID', table_header_style), Paragraph('Git Branch', table_header_style), Paragraph('Primary Functional Contribution', table_header_style)],
    [Paragraph('1', table_cell_bold), Paragraph('Harshita Upadhyay (TL)', table_cell_bold), Paragraph('BCS2025411', table_cell_bold), Paragraph('Harshita', table_cell_bold), Paragraph('Team Leader &amp; Architect: Git governance, integration &amp; delivery.', table_cell_style)],
    [Paragraph('2', table_cell_style), Paragraph('Lokesh Shukla', table_cell_style), Paragraph('BCS2025401', table_cell_style), Paragraph('Lokesh', table_cell_style), Paragraph('Backend Core Developer: Flask routing and exception handling.', table_cell_style)],
    [Paragraph('3', table_cell_style), Paragraph('Sudhanshu Singh', table_cell_style), Paragraph('BCS2025402', table_cell_style), Paragraph('Sudhanshu', table_cell_style), Paragraph('USP Research Lead: Data-Driven Career Intelligence proposition.', table_cell_style)],
    [Paragraph('4', table_cell_style), Paragraph('Rishabh Gupta', table_cell_style), Paragraph('BCS2025406', table_cell_style), Paragraph('Rishabh', table_cell_style), Paragraph('Dataset Engineering: Schema definition &amp; column specifications.', table_cell_style)],
    [Paragraph('5', table_cell_style), Paragraph('Anurag Verma', table_cell_style), Paragraph('BCS2025409', table_cell_style), Paragraph('Anurag', table_cell_style), Paragraph('Data Preprocessing Specialist: Regex design &amp; text sanitation.', table_cell_style)],
    [Paragraph('6', table_cell_style), Paragraph('Zainul Ali', table_cell_style), Paragraph('BCS2025413', table_cell_style), Paragraph('Zainul', table_cell_style), Paragraph('Frontend UI Lead: CSS Grid/Flexbox design and responsive layouts.', table_cell_style)],
    [Paragraph('7', table_cell_style), Paragraph('Ayushi', table_cell_style), Paragraph('BCS2025414', table_cell_style), Paragraph('Ayushi', table_cell_style), Paragraph('Frontend DOM Integration: Asynchronous data binding &amp; state handling.', table_cell_style)],
    [Paragraph('8', table_cell_style), Paragraph('Nilansh Gupta', table_cell_style), Paragraph('BCS2025416', table_cell_style), Paragraph('Nilansh', table_cell_style), Paragraph('Deployment &amp; Performance: Cloud deployment on Render, Gunicorn WSGI, LRU cache.', table_cell_style)],
    [Paragraph('9', table_cell_style), Paragraph('Pranay Kesarwani', table_cell_style), Paragraph('BCS2025417', table_cell_style), Paragraph('Pranay', table_cell_style), Paragraph('Directory Architecture Lead: Folder structure design &amp; governance.', table_cell_style)],
    [Paragraph('10', table_cell_style), Paragraph('Mohammad Muneer', table_cell_style), Paragraph('BCS2025418', table_cell_style), Paragraph('Muneer', table_cell_style), Paragraph('Experience Analytics: Range extraction &amp; statistical averages.', table_cell_style)],
    [Paragraph('11', table_cell_style), Paragraph('Kavyansh Bhadri', table_cell_style), Paragraph('BCS2025419', table_cell_style), Paragraph('Kavyansh', table_cell_style), Paragraph('City Normalization: Comma parsing &amp; location token ranking.', table_cell_style)],
    [Paragraph('12', table_cell_style), Paragraph('Abhay', table_cell_style), Paragraph('BCS2025421', table_cell_style), Paragraph('Abhay', table_cell_style), Paragraph('Fullstack Feature Engineer: Form search filter integration.', table_cell_style)],
    [Paragraph('13', table_cell_style), Paragraph('Sarvesh Singh', table_cell_style), Paragraph('BCS2025422', table_cell_style), Paragraph('Sarvesh', table_cell_style), Paragraph('QA &amp; Technical Governance: Glossary preparation &amp; code quality.', table_cell_style)],
    [Paragraph('14', table_cell_style), Paragraph('Sachin', table_cell_style), Paragraph('BCS2025424', table_cell_style), Paragraph('Sachin', table_cell_style), Paragraph('Salary Ethics Lead: Missing-value audit &amp; ethics disclosure.', table_cell_style)],
]

t = Table(team_data, colWidths=[24, 115, 62, 58, 256])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('GRID', (0,0), (-1,-1), 0.5, border_color),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('PADDING', (0,0), (-1,-1), 2.8),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#fbfcfe')]),
]))
story.append(t)
story.append(Spacer(1, 8))

# Abstract & Problem Statement
story.append(Paragraph('1. Executive Abstract &amp; Problem Statement', h1_style))
story.append(Paragraph('Undergraduate engineering students frequently struggle to identify which technical skills are most relevant to current industry demands. Informal guidance often reflects personal biases or outdated academic syllabi. Furthermore, online recruitment portals contain noisy abbreviations, multi-city listings, and unadvertised salary figures. The <b>Job Market Skills and Salary Analysis</b> project addresses this challenge through <b>Data-Driven Career Intelligence</b>, analyzing <b>12,000 real job postings</b> from Naukri across India to provide empirical insights into skill demand, role distributions, and location trends.', body_style))

story.append(Paragraph('2. Key Project Objectives', h1_style))
story.append(Paragraph('• <b>Automated Preprocessing:</b> Ingest, sanitize, and deduplicate 12,000 job advertisements.<br/>• <b>Skill Standardization:</b> Consolidate variants (Python, SQL, AWS, Machine Learning) using deterministic alias dictionaries.<br/>• <b>Entity &amp; City Normalization:</b> Resolve city aliases (e.g. Bangalore/Bengaluru -> Bengaluru) and create regional clusters (Delhi NCR).<br/>• <b>Role Taxonomy:</b> Classify diverse job titles into 18 established industry families.<br/>• <b>Experience Modeling:</b> Extract minimum and maximum experience thresholds using regular expressions.<br/>• <b>Salary Transparency:</b> Explicitly declare missing salary data rather than synthesizing misleading predictions.<br/>• <b>Cloud Deployment:</b> Deploy a high-performance Flask + Gunicorn web service on Render with sub-15ms response latency.', body_style))

story.append(PageBreak())

# Page 2: Architecture & Results
story.append(Paragraph('3. System Architecture &amp; Methodology', h1_style))
story.append(Paragraph('The application employs a decoupled client-server architecture. The backend is built using <b>Flask 3.x</b> and <b>Pandas 2.x</b>, served via <b>Gunicorn WSGI</b> on the <b>Render Cloud Platform</b>. Data loading is secured with an in-memory <b>LRU Cache</b> (@lru_cache) ensuring lightning-fast REST responses (&lt;15ms). The presentation tier employs semantic HTML5, modern CSS Grid/Flexbox, and asynchronous vanilla JavaScript (ES6+), eliminating unnecessary bundling overhead.', body_style))

story.append(Paragraph('4. Empirical Findings &amp; Quantitative Results', h1_style))

results_data = [
    [Paragraph('Analytical Dimension', table_header_style), Paragraph('Key Metric / Finding', table_header_style), Paragraph('Career &amp; Engineering Insight', table_header_style)],
    [Paragraph('Dataset Volume', table_cell_bold), Paragraph('12,000 Records (5 Dimensions)', table_cell_style), Paragraph('Large-scale sample of the Indian analytics and software ecosystem.', table_cell_style)],
    [Paragraph('Top In-Demand Skill', table_cell_bold), Paragraph('Python (>1,500 mentions)', table_cell_style), Paragraph('Foundational language required across ML, Data Engineering, and Analysis.', table_cell_style)],
    [Paragraph('Secondary Skills', table_cell_bold), Paragraph('SQL, ML, AWS, Excel, Power BI', table_cell_style), Paragraph('High industry emphasis on database querying, cloud deployment, and BI.', table_cell_style)],
    [Paragraph('Leading Tech Hub', table_cell_bold), Paragraph('Bengaluru (5,093 mentions)', table_cell_style), Paragraph('Accounts for ~42% of all localized technical job listings in India.', table_cell_style)],
    [Paragraph('Secondary Hubs', table_cell_bold), Paragraph('Pune (2,014), Hyderabad (1,940)', table_cell_style), Paragraph('Strong regional hiring demand in western and southern technology corridors.', table_cell_style)],
    [Paragraph('Prominent Role Family', table_cell_bold), Paragraph('Data Engineer (~27% of dataset)', table_cell_style), Paragraph('Substantial enterprise requirement for scalable ETL and cloud pipelines.', table_cell_style)],
    [Paragraph('Experience Requirement', table_cell_bold), Paragraph('Min: 2.8 yrs | Max: 6.4 yrs', table_cell_style), Paragraph('Entry-level roles (0-2 yrs) represent ~18%, requiring strong portfolio proof.', table_cell_style)],
    [Paragraph('Salary Transparency', table_cell_bold), Paragraph('0% Disclosed (Explicitly Disclaimed)', table_cell_style), Paragraph('Upholds academic integrity: zero fabricated or hallucinated salary metrics.', table_cell_style)],
]

rt = Table(results_data, colWidths=[115, 150, 250])
rt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), secondary_color),
    ('GRID', (0,0), (-1,-1), 0.5, border_color),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('PADDING', (0,0), (-1,-1), 3.5),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8faff')]),
]))
story.append(rt)
story.append(Spacer(1, 10))

story.append(Paragraph('5. Main Project USP: Data-Driven Career Intelligence', h1_style))
story.append(Paragraph('Our core innovation lies in bridging the gap between raw recruitment noise and student career planning. By substituting subjective guessing with empirical metrics derived from 12,000 real job ads, the platform empowers students to build a high-ROI learning roadmap. Furthermore, our anti-hallucination policy demonstrates professional data ethics by reporting missing compensation figures honestly rather than fabricating artificial numbers.', body_style))

story.append(Paragraph('6. Future Scope &amp; Enhancements', h1_style))
story.append(Paragraph('• <b>NLP Skill Extraction:</b> Implement Transformer-based Named Entity Recognition (NER) on full job descriptions.<br/>• <b>Resume Skill-Gap Matcher:</b> Provide an interactive tool allowing students to upload resumes and receive actionable skill-match percentages.<br/>• <b>Automated Pipeline Ingestion:</b> Implement scheduled cron jobs to ingest updated weekly job listings from authorized APIs.', body_style))

story.append(Paragraph('7. Conclusion', h1_style))
story.append(Paragraph('The <b>Job Market Skills and Salary Analysis</b> project provides an end-to-end demonstration of fullstack data engineering, robust API development, and data ethics. Completed by our 14-member student team under the guidance of Mr. Unwan Sir, the deployed platform serves as an accessible, high-performance career intelligence portal for engineering students.', body_style))

story.append(Spacer(1, 8))
story.append(HRFlowable(width='100%', thickness=1, color=border_color, spaceBefore=4, spaceAfter=8))
story.append(Paragraph('<b>Live Project URL:</b> <font color="#2457d6"><u>https://job-market-skills-and-salary-analysis.onrender.com/</u></font>', meta_style))
story.append(Paragraph('Academic Year 2026–2027 | CSED | Department of Computer Science and Engineering', meta_style))

doc.build(story)
print('Successfully generated PDF report at:', pdf_path)
print('File size:', os.path.getsize(pdf_path), 'bytes')

