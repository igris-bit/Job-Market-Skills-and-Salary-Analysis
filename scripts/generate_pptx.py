import os
import zipfile

os.makedirs('presentation', exist_ok=True)
pptx_path = os.path.join('presentation', 'Job_Market_Skills_and_Salary_Analysis_Presentation.pptx')

content_types_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
  <Override PartName="/ppt/slides/slide1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
  <Override PartName="/ppt/slides/slide2.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
  <Override PartName="/ppt/slides/slide3.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
  <Override PartName="/ppt/slides/slide4.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
  <Override PartName="/ppt/slides/slide5.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
  <Override PartName="/ppt/slides/slide6.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
  <Override PartName="/ppt/slides/slide7.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
</Types>"""

root_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>"""

pres_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide1.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide2.xml"/>
  <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide3.xml"/>
  <Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide4.xml"/>
  <Relationship Id="rId6" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide5.xml"/>
  <Relationship Id="rId7" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide6.xml"/>
  <Relationship Id="rId8" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide7.xml"/>
</Relationships>"""

presentation_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst>
    <p:sldMasterId id="2147483648" r:id="rId1" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
  </p:sldMasterIdLst>
  <p:sldIdLst>
    <p:sldId id="256" r:id="rId2" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
    <p:sldId id="257" r:id="rId3" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
    <p:sldId id="258" r:id="rId4" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
    <p:sldId id="259" r:id="rId5" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
    <p:sldId id="260" r:id="rId6" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
    <p:sldId id="261" r:id="rId7" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
    <p:sldId id="262" r:id="rId8" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
  </p:sldIdLst>
  <p:sldSz cx="9144000" cy="5143500" type="screen16x9"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>"""

theme_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme">
  <a:themeElements>
    <a:clrScheme name="Antigravity">
      <a:dk1><a:srgbClr val="17243B"/></a:dk1>
      <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="173EAA"/></a:dk2>
      <a:lt2><a:srgbClr val="F0F5FF"/></a:lt2>
      <a:accent1><a:srgbClr val="2457D6"/></a:accent1>
      <a:accent2><a:srgbClr val="10B981"/></a:accent2>
      <a:accent3><a:srgbClr val="F59E0B"/></a:accent3>
      <a:accent4><a:srgbClr val="EF4444"/></a:accent4>
      <a:accent5><a:srgbClr val="8B5CF6"/></a:accent5>
      <a:accent6><a:srgbClr val="06B6D4"/></a:accent6>
      <a:hlink><a:srgbClr val="2457D6"/></a:hlink>
      <a:folHlink><a:srgbClr val="173EAA"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="Office">
      <a:majorFont><a:latin typeface="Calibri"/></a:majorFont>
      <a:minorFont><a:latin typeface="Calibri"/></a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="Office">
      <a:fillStyleLst><a:solidFill><a:schemeClr val="lt1"/></a:solidFill></a:fillStyleLst>
      <a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst>
      <a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>
      <a:bgFillStyleLst><a:solidFill><a:schemeClr val="lt1"/></a:solidFill></a:bgFillStyleLst>
    </a:fmtScheme>
  </a:themeElements>
</a:theme>"""

slide_master_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst>
    <p:sldLayoutId id="2147483649" r:id="rId1" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
  </p:sldLayoutIdLst>
</p:sldMaster>"""

master_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>"""

layout_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank">
  <p:cSld name="Blank">
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>"""

layout_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>"""

slide_rel = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>"""

def make_slide(title, subtitle, bullets):
    bullet_xml = ""
    for b in bullets:
        bullet_xml += f"""
        <a:p>
          <a:pPr lvl="0"><a:buChar char="•"/></a:pPr>
          <a:r>
            <a:rPr lang="en-US" sz="1600" b="0"><a:solidFill><a:srgbClr val="334155"/></a:solidFill></a:rPr>
            <a:t>{b}</a:t>
          </a:r>
        </a:p>"""

    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      <!-- Title Box -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="Title"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="609600" y="457200"/><a:ext cx="7924800" cy="1143000"/></a:xfrm>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/>
          <a:p>
            <a:r>
              <a:rPr lang="en-US" sz="2800" b="1"><a:solidFill><a:srgbClr val="173EAA"/></a:solidFill></a:rPr>
              <a:t>{title}</a:t>
            </a:r>
          </a:p>
          <a:p>
            <a:r>
              <a:rPr lang="en-US" sz="1400" b="1"><a:solidFill><a:srgbClr val="2457D6"/></a:solidFill></a:rPr>
              <a:t>{subtitle}</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>
      <!-- Content Box -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Content"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="609600" y="1752600"/><a:ext cx="7924800" cy="3048000"/></a:xfrm>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/>
          {bullet_xml}
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>"""

slides_data = [
    (
        "Job Market Skills &amp; Salary Analysis",
        "B.Tech Computer Science &amp; Engineering — 2nd Year (DA-021)",
        [
            "Center for Skill and Entrepreneurship Development (CSED)",
            "Faculty Mentor: Mr. Unwan Sir",
            "Team Leader: Harshita Upadhyay (Student ID: BCS2025411)",
            "Live Deployed Project URL: https://job-market-skills-and-salary-analysis.onrender.com/",
            "Dataset: 12,000 Verified Naukri Job Postings across India"
        ]
    ),
    (
        "The Problem &amp; Industry Context",
        "Bridging Curriculum with Hiring Reality",
        [
            "Curriculum Misalignment: Engineering students face ambiguity about which tools employers require.",
            "Subjective Guidance: Social media opinions are anecdotal, unverified, and hype-driven.",
            "Recruitment Noise: Job postings feature messy abbreviations, multi-city strings, and vague titles.",
            "Fake Salary Predictions: Many projects invent synthetic salaries on datasets that lack salary data.",
            "Our Mission: Build a reproducible data science pipeline delivering empirical career intelligence."
        ]
    ),
    (
        "Main Project USP: Data-Driven Career Intelligence",
        "Evidence-Based Career Roadmaps for Students",
        [
            "Empirical Evidence: Frequency rankings across 12,000 postings guide high-ROI learning.",
            "Heuristic Normalization: Consolidates noisy variants (py -> Python, Bangalore -> Bengaluru).",
            "Conservative Role Taxonomy: 18 distinct role families group listings while preserving original titles.",
            "Anti-Hallucination Ethics: Transparently reports that salary data is unadvertised with zero fabrication."
        ]
    ),
    (
        "14-Member Team Roster &amp; Git Branches",
        "Collaborative Feature-Branch Architecture",
        [
            "Harshita Upadhyay (TL, BCS2025411) - Branch: Harshita | Architecture &amp; Governance",
            "Lokesh Shukla (BCS2025401) - Branch: Lokesh | Backend Core &amp; Flask API Routing",
            "Sudhanshu Singh (BCS2025402) - Branch: Sudhanshu | USP Formulation &amp; Research",
            "Rishabh Gupta (BCS2025406) - Branch: Rishabh | Dataset Engineering &amp; Schema",
            "Anurag Verma (BCS2025409) - Branch: Anurag | Regex Preprocessing &amp; Text Cleaning",
            "Zainul Ali (BCS2025413) - Branch: Zainul | Frontend CSS Grid/Flexbox UI",
            "Ayushi (BCS2025414) - Branch: Ayushi | Frontend DOM Data Binding &amp; State",
            "Nilansh Gupta (BCS2025416) - Branch: Nilansh | Render Deployment, Gunicorn &amp; Cache",
            "Pranay Kesarwani (BCS2025417) - Branch: Pranay | Folder Structure &amp; Governance",
            "Mohammad Muneer (BCS2025418) - Branch: Muneer | Experience Analytics &amp; Averages",
            "Kavyansh Bhadri (BCS2025419) - Branch: Kavyansh | City Normalization &amp; Tokenization",
            "Abhay (BCS2025421) - Branch: Abhay | Fullstack Search Filter Integration",
            "Sarvesh Singh (BCS2025422) - Branch: Sarvesh | QA Testing &amp; Technical Governance",
            "Sachin (BCS2025424) - Branch: Sachin | Salary Ethics Audit &amp; Boundary Verification"
        ]
    ),
    (
        "System Architecture &amp; Technology Stack",
        "High-Performance In-Memory Data Serving",
        [
            "Backend: Python 3.10+, Flask 3.x, Flask-CORS, Gunicorn WSGI Server.",
            "Data Engine: Pandas 2.x, Regular Expressions, functools.lru_cache for sub-15ms queries.",
            "Frontend: Semantic HTML5, Modern CSS Grid/Flexbox, Vanilla ES6 JavaScript (zero bloat).",
            "Cloud Infrastructure: Render Cloud Platform with automated build, HTTPS, and health checks."
        ]
    ),
    (
        "Empirical Findings from 12,000 Postings",
        "Key Career Signals from the Indian Tech Market",
        [
            "Top Skills: Python is #1 (>1,500 mentions), followed by SQL, Machine Learning, AWS, and Excel.",
            "Hiring Hubs: Bengaluru leads with 5,093 mentions (~42%), followed by Pune (2,014) and Hyderabad (1,940).",
            "Role Breakdown: Data Engineer is #1 (~27%), followed by Data Scientist (~11%) and Analysts (~15%).",
            "Experience: Average minimum is 2.8 years, maximum is 6.4 years; Entry-level is ~18%.",
            "Salary: 0% disclosed; platform displays clear transparency notice to prevent misleading expectations."
        ]
    ),
    (
        "Live Demonstration &amp; Conclusion",
        "Interactive Production Dashboard on Render",
        [
            "Live URL: https://job-market-skills-and-salary-analysis.onrender.com/",
            "Key Features: Dynamic search filters, responsive cards, client pagination, and live status.",
            "Future Scope: Transformer-based NLP extraction and automated student resume skill-gap matching.",
            "Thank you to Faculty Mentor Mr. Unwan Sir and examiners for this evaluation opportunity!"
        ]
    )
]

with zipfile.ZipFile(pptx_path, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', content_types_xml)
    z.writestr('_rels/.rels', root_rels)
    z.writestr('ppt/presentation.xml', presentation_xml)
    z.writestr('ppt/_rels/presentation.xml.rels', pres_rels)
    z.writestr('ppt/theme/theme1.xml', theme_xml)
    z.writestr('ppt/slideMasters/slideMaster1.xml', slide_master_xml)
    z.writestr('ppt/slideMasters/_rels/slideMaster1.xml.rels', master_rels)
    z.writestr('ppt/slideLayouts/slideLayout1.xml', layout_xml)
    z.writestr('ppt/slideLayouts/_rels/slideLayout1.xml.rels', layout_rels)
    for i, (title, subtitle, bullets) in enumerate(slides_data, start=1):
        z.writestr(f'ppt/slides/slide{i}.xml', make_slide(title, subtitle, bullets))
        z.writestr(f'ppt/slides/_rels/slide{i}.xml.rels', slide_rel)

print('Successfully generated PowerPoint presentation at:', pptx_path)
print('File size:', os.path.getsize(pptx_path), 'bytes')

