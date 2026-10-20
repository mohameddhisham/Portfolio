import base64
import textwrap
from pathlib import Path

import streamlit as st

BASE = Path(__file__).parent

# ----------------------------------------------------------------------------
# COLORS — deep, saturated tones (no pastels). Change them here.
# ----------------------------------------------------------------------------
TEAL = "#0d9488"
INDIGO = "#4f46e5"
BLUE = "#2563eb"
AMBER = "#d97706"
ROSE = "#e11d48"
VIOLET = "#7c3aed"

# ----------------------------------------------------------------------------
# CONTENT — edit everything here, the page below is generated from it.
# ----------------------------------------------------------------------------
NAME = "Mohamed Hisham Ibrahim"
TITLE = "Data Analyst"
LOCATION = "Cairo, Egypt"
EMAIL = "mohamedhisha77@gmail.com"
PHONES = ["01062911800", "01115846343"]
LINKEDIN = "https://linkedin.com/in/mohamed-hisham-ibrahim"
GITHUB = "https://github.com/mohameddhisham"
CV_URL = "https://drive.google.com/file/d/14k79JMHA4XWFN5u97Yr9T6HqbYIQ4tGv/view?usp=sharing"

TAGLINE = (
    "I turn complex data into clear, actionable insights — through ETL pipelines, "
    "automated reporting and interactive dashboards."
)

ABOUT = (
    "I am a Data Analyst proficient in Python, SQL, Power BI, Looker Studio, Tableau, "
    "DAX and data warehousing. I design and optimize ETL processes and interactive "
    "dashboards that help teams make strategic business decisions, enhance data "
    "accessibility and streamline workflows."
)

METRICS = [
    ("11M+", "records processed in Python", TEAL),
    ("1000+", "users reached by dashboards", AMBER),
    ("25%", "less data processing time", BLUE),
    ("100%", "data integrity for reporting", ROSE),
]

EXPERIENCE = [
    {
        "role": "Data Analyst",
        "company": "Mismar",
        "period": "Feb 2026 – Present",
        "color": TEAL,
        "points": [
            "Extract and analyze data using MySQL and Google BigQuery",
            "Build and maintain dashboards using Metabase, Looker Studio and Power BI",
            "Automate workflows and reporting processes using Zapier",
            "Perform data analysis using Python and advanced Excel",
            "Identify trends, patterns and performance gaps",
            "Translate business requirements into analytical reports and present insights to stakeholders",
        ],
    },
    {
        "role": "Real Time Analyst",
        "company": "Outsourcing Skill",
        "period": "Sep 2022 – Mar 2026",
        "color": INDIGO,
        "points": [
            "Streamlined repetitive data collection tasks using Python and Excel to increase team efficiency",
            "Analyzed data from various sources to improve call center performance metrics",
            "Collaborated with cross-functional teams on visualization solutions reaching 1000+ users",
            "Developed and maintained complex data models, cutting data processing time by 25%",
            "Performed ETL to clean and structure raw data, ensuring 100% data integrity for downstream reporting",
        ],
    },
]

PROJECTS = [
    {
        "name": "Retail Sales Performance Dashboard",
        "badge": "Featured · Interactive",
        "color": TEAL,
        "stack": ["Python", "Pandas", "Plotly", "Streamlit"],
        "desc": (
            "An interactive sales analytics dashboard: KPI cards with period-over-period "
            "change, revenue and profit trends, category / channel / region breakdowns, "
            "a top-products table and filters by date, region, category and channel. "
            "Built on a synthetic sample dataset of ~130K orders."
        ),
        "page": "pages/1_Sales_Dashboard.py",
    },
    {
        "name": "Automated Lead Filtration System",
        "color": INDIGO,
        "stack": ["Python", "Pandas"],
        "desc": (
            "Reads large CSV files of lead data with Pandas, cleans missing values and "
            "inconsistencies, then filters leads through a flexible mechanism that compares "
            "lead dispositions against a configurable list of unwanted statuses."
        ),
        "link": "",  # TODO: GitHub repo URL
    },
    {
        "name": "Data Quality Analysis",
        "color": AMBER,
        "stack": ["Python", "Pandas"],
        "desc": (
            "Processed a dataset of 11 million records and used cleaning and filtering "
            "techniques to uncover consistent patterns of duplicate leads sent by a vendor."
        ),
        "link": "",  # TODO: GitHub repo URL
    },
]

SKILLS = {
    "Languages & Querying": (["Python", "SQL", "DAX", "Pandas"], TEAL),
    "BI & Visualization": (["Power BI", "Tableau", "Looker Studio", "Metabase", "Excel"], INDIGO),
    "Data & Automation": (["MySQL", "BigQuery", "ETL", "Data Warehousing", "Zapier"], AMBER),
    "Soft Skills": (["Communication", "Time Management", "Stakeholder Reporting"], ROSE),
}

EDUCATION = {
    "school": "Helwan University",
    "degree": "Bachelor of Business Information Systems",
    "period": "2019 – 2023",
    "note": "GPA: 3.41 (Excellent)",
}

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title=f"{NAME} | {TITLE}",
    page_icon="📊",
    layout="centered",
)


def html(s: str):
    st.markdown(textwrap.dedent(s).strip(), unsafe_allow_html=True)


def chips(items, color):
    return "".join(
        f'<span class="chip" style="border-color:{color};background:{color}26">{i}</span>'
        for i in items
    )


def photo_uri():
    """Looks for assets/profile.(jpg|jpeg|png|webp) and embeds it. Returns None if absent."""
    for ext in ("jpg", "jpeg", "png", "webp"):
        p = BASE / "assets" / f"profile.{ext}"
        if p.exists():
            mime = "jpeg" if ext in ("jpg", "jpeg") else ext
            return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"
    return None


html(
    """
<style>
.block-container {padding-top: 2.5rem; max-width: 860px;}
.hero {display:flex; align-items:center; gap:1.6rem; flex-wrap:wrap; margin-bottom:.4rem;}
.avatar {width:132px; height:132px; border-radius:50%; object-fit:cover;
         border:3px solid #0d9488; box-shadow:0 0 0 5px #4f46e533;}
.name {font-size:2.6rem; font-weight:800; margin:0; padding:0; line-height:1.1;
       background:linear-gradient(90deg,#6366f1,#0d9488); -webkit-background-clip:text;
       background-clip:text; color:transparent;}
.subtitle {font-size:1.3rem; color:#0d9488; font-weight:600; margin:.3rem 0 .4rem 0;}
.tagline {font-size:1.05rem; opacity:.85; margin:0;}
.chip {display:inline-block; padding:3px 12px; margin:3px 4px 3px 0; border-radius:999px;
       border:1px solid; font-size:.85rem; color:#e6edf7;}
.card {border:1px solid #1f2a44; border-left:5px solid #0d9488; border-radius:14px;
       padding:1.1rem 1.3rem; margin-bottom:1rem;
       background:linear-gradient(135deg,#111a2b,#0d1424);}
.card h4 {margin:0 0 .15rem 0;}
.muted {opacity:.65; font-size:.9rem;}
.metric {border-top:4px solid; padding-top:.5rem;}
.metric-num {font-size:2.1rem; font-weight:800; line-height:1.1;}
.badge {display:inline-block; padding:2px 10px; border-radius:6px; font-size:.75rem;
        font-weight:700; letter-spacing:.03em; color:#fff; margin-bottom:.3rem;}
[data-testid="stLinkButton"], [data-testid="stLinkButton"] a {width:100%;}
[data-testid="stLinkButton"] a {justify-content:center;}
h2 {border-bottom:2px solid #1f2a44; padding-bottom:.3rem;}
a {text-decoration:none;}
</style>
"""
)

# --- Hero -------------------------------------------------------------------
photo = photo_uri()
img = f'<img class="avatar" src="{photo}" alt="{NAME}">' if photo else ""
html(
    f"""
<div class="hero">{img}<div>
<h1 class="name">{NAME}</h1>
<p class="subtitle">{TITLE} · {LOCATION}</p>
<p class="tagline">{TAGLINE}</p>
</div></div>
"""
)

b1, b2, b3, b4 = st.columns(4)
b1.link_button("📄 Download CV", CV_URL)
b2.link_button("💼 LinkedIn", LINKEDIN)
b3.link_button("🐙 GitHub", GITHUB)
b4.link_button("✉️ Email me", f"mailto:{EMAIL}")

st.divider()

# --- Metrics ----------------------------------------------------------------
cols = st.columns(len(METRICS))
for col, (num, label, color) in zip(cols, METRICS):
    col.markdown(
        f'<div class="metric" style="border-color:{color}">'
        f'<div class="metric-num" style="color:{color}">{num}</div>'
        f'<div class="muted">{label}</div></div>',
        unsafe_allow_html=True,
    )

# --- About ------------------------------------------------------------------
st.header("About")
st.write(ABOUT)

# --- Projects ---------------------------------------------------------------
st.header("Projects")
for p in PROJECTS:
    color = p.get("color", TEAL)
    with st.container(border=True):
        if p.get("badge"):
            html(f'<span class="badge" style="background:{color}">{p["badge"]}</span>')
        if p.get("image"):
            st.image(p["image"])
        st.subheader(p["name"])
        st.markdown(chips(p["stack"], color), unsafe_allow_html=True)
        st.write(p["desc"])
        if p.get("page"):
            st.page_link(p["page"], label="Open the live dashboard", icon="📈")
        if p.get("link"):
            st.link_button("View project", p["link"])

# --- Experience -------------------------------------------------------------
st.header("Experience")
for job in EXPERIENCE:
    bullets = "".join(f"<li>{pt}</li>" for pt in job["points"])
    html(
        f"""
<div class="card" style="border-left-color:{job['color']}">
<h4>{job['role']} · <span style="color:{job['color']}">{job['company']}</span></h4>
<div class="muted">{job['period']}</div>
<ul style="margin-top:.6rem">{bullets}</ul>
</div>
"""
    )

# --- Skills -----------------------------------------------------------------
st.header("Skills")
for group, (items, color) in SKILLS.items():
    st.markdown(f"**{group}**")
    st.markdown(chips(items, color), unsafe_allow_html=True)

# --- Education --------------------------------------------------------------
st.header("Education")
html(
    f"""
<div class="card" style="border-left-color:{AMBER}">
<h4>{EDUCATION['school']}</h4>
<div>{EDUCATION['degree']}</div>
<div class="muted">{EDUCATION['period']} · {EDUCATION['note']}</div>
</div>
"""
)

# --- Contact ----------------------------------------------------------------
st.header("Contact")
st.markdown(
    f"""
- 📧 [{EMAIL}](mailto:{EMAIL})
- 📞 {" / ".join(PHONES)}
- 💼 [LinkedIn]({LINKEDIN})
- 🐙 [GitHub]({GITHUB})
"""
)
st.caption(f"© {NAME} · Built with Python & Streamlit")
