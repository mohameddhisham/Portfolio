import streamlit as st

# ----------------------------------------------------------------------------
# CONTENT — edit everything here, the page below is generated from it.
# Anything marked TODO is not in the CV yet; fill it in or leave it empty
# and the section will hide itself.
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

# TODO: replace/extend with numbers you are comfortable showing
METRICS = [
    ("11M+", "records processed in Python"),
    ("1000+", "users reached by dashboards"),
    ("25%", "less data processing time"),
    ("100%", "data integrity for reporting"),
]

EXPERIENCE = [
    {
        "role": "Data Analyst",
        "company": "Mismar",
        "period": "Feb 2026 – Present",
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
        "name": "Automated Lead Filtration System",
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
        "stack": ["Python", "Pandas"],
        "desc": (
            "Processed a dataset of 11 million records and used cleaning and filtering "
            "techniques to uncover consistent patterns of duplicate leads sent by a vendor."
        ),
        "link": "",  # TODO: GitHub repo URL
    },
    # TODO: add 2-3 dashboard projects (Power BI / Tableau / Looker Studio)
    # with a screenshot and a public link. Example:
    # {"name": "Sales Dashboard", "stack": ["Power BI", "DAX"], "desc": "...",
    #  "link": "https://...", "image": "assets/sales.png"},
]

SKILLS = {
    "Languages & Querying": ["Python", "SQL", "DAX", "Pandas"],
    "BI & Visualization": ["Power BI", "Tableau", "Looker Studio", "Metabase", "Excel"],
    "Data & Automation": ["MySQL", "BigQuery", "ETL", "Data Warehousing", "Zapier"],
    "Soft Skills": ["Communication", "Time Management", "Stakeholder Reporting"],
}

EDUCATION = {
    "school": "Helwan University",
    "degree": "Bachelor of Business Information Systems",
    "period": "2019 – 2023",
    "note": "GPA: 3.41 (Excellent)",
}

# ----------------------------------------------------------------------------
# PAGE
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title=f"{NAME} | {TITLE}",
    page_icon="📊",
    layout="centered",
)

st.markdown(
    """
    <style>
    .block-container {padding-top: 2.5rem; max-width: 860px;}
    h1 {font-size: 2.6rem !important; margin-bottom: 0;}
    .subtitle {font-size: 1.35rem; color: #7ee0c3; margin: 0 0 .6rem 0;}
    .tagline {font-size: 1.05rem; opacity: .85; margin-bottom: 1rem;}
    .chip {display:inline-block; padding: 3px 12px; margin: 3px 4px 3px 0;
           border-radius: 999px; border: 1px solid #2f6f5e; background:#12302a;
           font-size:.85rem;}
    .card {border:1px solid #26332f; border-radius:14px; padding:1.1rem 1.3rem;
           margin-bottom:1rem; background:#0f1a17;}
    .card h4 {margin:0 0 .15rem 0;}
    .muted {opacity:.65; font-size:.9rem;}
    .metric-num {font-size:2rem; font-weight:700; color:#7ee0c3; line-height:1.1;}
    a {text-decoration:none;}
    </style>
    """,
    unsafe_allow_html=True,
)


def chips(items):
    return "".join(f'<span class="chip">{i}</span>' for i in items)


# --- Hero -------------------------------------------------------------------
st.title(NAME)
st.markdown(f'<p class="subtitle">{TITLE} · {LOCATION}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="tagline">{TAGLINE}</p>', unsafe_allow_html=True)

b1, b2, b3, b4 = st.columns(4)
b1.link_button("📄 Download CV", CV_URL, use_container_width=True)
b2.link_button("💼 LinkedIn", LINKEDIN, use_container_width=True)
b3.link_button("🐙 GitHub", GITHUB, use_container_width=True)
b4.link_button("✉️ Email me", f"mailto:{EMAIL}", use_container_width=True)

st.divider()

# --- Metrics ----------------------------------------------------------------
cols = st.columns(len(METRICS))
for col, (num, label) in zip(cols, METRICS):
    col.markdown(
        f'<div class="metric-num">{num}</div><div class="muted">{label}</div>',
        unsafe_allow_html=True,
    )

# --- About ------------------------------------------------------------------
st.header("About")
st.write(ABOUT)

# --- Experience -------------------------------------------------------------
st.header("Experience")
for job in EXPERIENCE:
    bullets = "".join(f"<li>{p}</li>" for p in job["points"])
    st.markdown(
        f"""
        <div class="card">
          <h4>{job['role']} · {job['company']}</h4>
          <div class="muted">{job['period']}</div>
          <ul style="margin-top:.6rem">{bullets}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Projects ---------------------------------------------------------------
if PROJECTS:
    st.header("Projects")
    for p in PROJECTS:
        with st.container(border=True):
            if p.get("image"):
                st.image(p["image"], use_container_width=True)
            st.subheader(p["name"])
            st.markdown(chips(p["stack"]), unsafe_allow_html=True)
            st.write(p["desc"])
            if p.get("link"):
                st.link_button("View project", p["link"])

# --- Skills -----------------------------------------------------------------
st.header("Skills")
for group, items in SKILLS.items():
    st.markdown(f"**{group}**")
    st.markdown(chips(items), unsafe_allow_html=True)

# --- Education --------------------------------------------------------------
st.header("Education")
st.markdown(
    f"""
    <div class="card">
      <h4>{EDUCATION['school']}</h4>
      <div>{EDUCATION['degree']}</div>
      <div class="muted">{EDUCATION['period']} · {EDUCATION['note']}</div>
    </div>
    """,
    unsafe_allow_html=True,
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
