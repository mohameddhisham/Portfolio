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

# Dashboard screenshots. Upload each image as <image>.png (or .jpg/.webp) into
# assets/ — a card only shows up once its image file exists.
# TODO: set a real title, tools and one-line description for each dashboard.
GALLERY = [
    {"title": "Dashboard 1", "tools": [], "desc": "", "color": TEAL, "image": "dashboard1"},
    {"title": "Dashboard 2", "tools": [], "desc": "", "color": INDIGO, "image": "dashboard2"},
]

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title=f"{NAME} | {TITLE}",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


def html(s: str):
    st.markdown(textwrap.dedent(s).strip(), unsafe_allow_html=True)


def section(title: str, color: str):
    html(f'<h2 class="sec" style="border-left-color:{color}">{title}</h2>')


def chips(items, color):
    return "".join(
        f'<span class="chip" style="border-color:{color};background:{color}33">{i}</span>'
        for i in items
    )


def find_image(stem: str):
    """Looks for <stem>.(jpg|jpeg|png|webp) in assets/ or the repo root."""
    for folder in (BASE / "assets", BASE):
        for ext in ("jpg", "jpeg", "png", "webp"):
            p = folder / f"{stem}.{ext}"
            if p.exists():
                return p
    return None


def photo_uri():
    p = find_image("profile")
    if not p:
        return None
    mime = "jpeg" if p.suffix.lower() in (".jpg", ".jpeg") else p.suffix.lower().lstrip(".")
    return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"


html(
    """
<style>
.stApp {
  background:
    radial-gradient(900px 520px at 0% 0%, rgba(79,70,229,.38), transparent 60%),
    radial-gradient(800px 500px at 100% 8%, rgba(13,148,136,.30), transparent 60%),
    radial-gradient(900px 600px at 50% 100%, rgba(124,58,237,.28), transparent 60%),
    radial-gradient(700px 500px at 0% 70%, rgba(37,99,235,.18), transparent 60%),
    #0a0f1a;
  background-attachment: fixed;
}
[data-testid="stHeader"] {background: transparent;}
.block-container {padding: 2.2rem 4rem 3rem 4rem; max-width: 1400px;}
@media (max-width: 800px) {.block-container {padding: 1.5rem 1rem;}}

.hero {display:flex; align-items:center; gap:2rem; flex-wrap:wrap; padding:2rem 2.4rem;
       border-radius:22px; border:1px solid rgba(99,102,241,.45);
       background:linear-gradient(120deg, rgba(79,70,229,.45), rgba(13,148,136,.35));
       box-shadow:0 10px 40px rgba(0,0,0,.35); margin-bottom:1rem;}
.avatar {width:150px; height:150px; border-radius:50%; object-fit:cover;
         border:4px solid #0d9488; box-shadow:0 0 0 6px rgba(255,255,255,.12);}
.name {font-size:3rem; font-weight:800; margin:0; padding:0; line-height:1.1; color:#fff;}
.subtitle {font-size:1.35rem; color:#fff; opacity:.92; font-weight:600; margin:.4rem 0 .5rem 0;}
.tagline {font-size:1.1rem; color:#fff; opacity:.8; margin:0; max-width:760px;}

h2.sec {border-left:6px solid #0d9488; padding:.1rem 0 .1rem .8rem; margin:2rem 0 1rem 0;
        font-size:1.7rem;}
.chip {display:inline-block; padding:3px 12px; margin:3px 4px 3px 0; border-radius:999px;
       border:1px solid; font-size:.85rem; color:#e6edf7;}
.card {border:1px solid #1f2a44; border-left:5px solid #0d9488; border-radius:14px;
       padding:1.2rem 1.4rem; margin-bottom:1rem; height:100%;
       background:rgba(14,22,40,.78);}
.card h4 {margin:0 0 .15rem 0;}
.muted {opacity:.65; font-size:.9rem;}
.panel {border:1px solid #1f2a44; border-top:4px solid; border-radius:14px;
        padding:1rem 1.3rem; background:rgba(14,22,40,.78);}
.metric-num {font-size:2.3rem; font-weight:800; line-height:1.1;}
.badge {display:inline-block; padding:2px 10px; border-radius:6px; font-size:.75rem;
        font-weight:700; letter-spacing:.03em; color:#fff; margin-bottom:.3rem;}
[data-testid="stVerticalBlockBorderWrapper"] {background:rgba(14,22,40,.78);
        border-color:#1f2a44; border-radius:14px;}
[data-testid="stLinkButton"], [data-testid="stLinkButton"] a {width:100%;}
[data-testid="stLinkButton"] a {justify-content:center;}
a {text-decoration:none;}

/* ---- Sidebar menu (big and visible) ---- */
[data-testid="stSidebarNav"] {display:none;}
[data-testid="stSidebar"] {background:linear-gradient(180deg,#17154a 0%,#0b2a2c 100%);
        border-right:1px solid rgba(99,102,241,.35);}
[data-testid="stSidebar"][aria-expanded="true"] {min-width:300px; max-width:300px;}
.side-title {font-size:.8rem; letter-spacing:.16em; text-transform:uppercase; opacity:.7;
        margin:.4rem 0 .7rem 0; font-weight:700;}
[data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"],
[data-testid="stSidebar"] [data-testid="stPageLink"] a {
        padding:.9rem 1.1rem; margin-bottom:.55rem; border-radius:12px;
        background:rgba(255,255,255,.07); border:1px solid rgba(99,102,241,.55);}
[data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"] p,
[data-testid="stSidebar"] [data-testid="stPageLink"] a p {font-size:1.2rem !important; font-weight:700;}
[data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"]:hover,
[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {background:rgba(13,148,136,.5);}
[data-testid="stSidebar"] a[aria-current="page"] {background:#0d9488; border-color:#0d9488;}
</style>
"""
)

# --- Sidebar menu -----------------------------------------------------------
with st.sidebar:
    html('<div class="side-title">Menu</div>')
    st.page_link("app.py", label="Portfolio", icon="🏠")
    if (BASE / "pages" / "1_Sales_Dashboard.py").exists():
        st.page_link("pages/1_Sales_Dashboard.py", label="Sales Dashboard", icon="📈")

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

# --- Metrics ----------------------------------------------------------------
st.write("")
cols = st.columns(len(METRICS), gap="medium")
for col, (num, label, color) in zip(cols, METRICS):
    col.markdown(
        f'<div class="panel" style="border-top-color:{color}">'
        f'<div class="metric-num" style="color:{color}">{num}</div>'
        f'<div class="muted">{label}</div></div>',
        unsafe_allow_html=True,
    )

# --- About + Education ------------------------------------------------------
left, right = st.columns([3, 2], gap="large")
with left:
    section("About", TEAL)
    html(f'<div class="card" style="font-size:1.05rem;line-height:1.7">{ABOUT}</div>')
with right:
    section("Education", AMBER)
    html(
        f"""
<div class="card" style="border-left-color:{AMBER}">
<h4>{EDUCATION['school']}</h4>
<div>{EDUCATION['degree']}</div>
<div class="muted">{EDUCATION['period']} · {EDUCATION['note']}</div>
</div>
"""
    )

# --- Projects ---------------------------------------------------------------
section("Projects", INDIGO)


def project_card(p):
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
            if (BASE / p["page"]).exists():
                st.page_link(p["page"], label="Open the live dashboard", icon="📈")
            else:
                st.caption("Dashboard page is missing from the repo: pages/1_Sales_Dashboard.py")
        if p.get("link"):
            st.link_button("View project", p["link"])


featured = [p for p in PROJECTS if p.get("badge")]
others = [p for p in PROJECTS if not p.get("badge")]
for p in featured:
    project_card(p)
pcols = st.columns(2, gap="large")
for i, p in enumerate(others):
    with pcols[i % 2]:
        project_card(p)

# --- Dashboards gallery -----------------------------------------------------
gallery = [(g, find_image(g["image"])) for g in GALLERY]
gallery = [(g, path) for g, path in gallery if path]
if gallery:
    section("Dashboards", TEAL)
    gcols = st.columns(2, gap="large")
    for i, (g, path) in enumerate(gallery):
        with gcols[i % 2]:
            with st.container(border=True):
                st.image(str(path))
                st.subheader(g["title"])
                if g.get("tools"):
                    st.markdown(chips(g["tools"], g["color"]), unsafe_allow_html=True)
                if g.get("desc"):
                    st.write(g["desc"])

# --- Experience -------------------------------------------------------------
section("Experience", BLUE)
ecols = st.columns(len(EXPERIENCE), gap="large")
for col, job in zip(ecols, EXPERIENCE):
    bullets = "".join(f"<li>{pt}</li>" for pt in job["points"])
    with col:
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
section("Skills", VIOLET)
scols = st.columns(2, gap="large")
for i, (group, (items, color)) in enumerate(SKILLS.items()):
    with scols[i % 2]:
        html(
            f"""
<div class="card" style="border-left-color:{color}">
<b>{group}</b><br>{chips(items, color)}
</div>
"""
        )

# --- Contact ----------------------------------------------------------------
section("Contact", ROSE)
contacts = [
    ("Email", f'<a href="mailto:{EMAIL}">{EMAIL}</a>', TEAL),
    ("Phone", " / ".join(PHONES), AMBER),
    ("LinkedIn", f'<a href="{LINKEDIN}">mohamed-hisham-ibrahim</a>', BLUE),
    ("GitHub", f'<a href="{GITHUB}">mohameddhisham</a>', INDIGO),
]
ccols = st.columns(4, gap="medium")
for col, (label, value, color) in zip(ccols, contacts):
    col.markdown(
        f'<div class="panel" style="border-top-color:{color}">'
        f'<div class="muted">{label}</div><div>{value}</div></div>',
        unsafe_allow_html=True,
    )

st.write("")
st.caption(f"© {NAME} · Built with Python & Streamlit")
