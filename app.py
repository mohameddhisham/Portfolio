import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page configuration with custom branding
st.set_page_config(
    page_title="Mohamed Hisham | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hero section badge styling */
    .hero-badge {
        display: inline-block;
        padding: 4px 12px;
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(14, 165, 233, 0.15));
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 9999px;
        color: #3b82f6;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 12px;
    }

    /* Metric cards styling */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-4px);
        border-color: #3b82f6;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #3b82f6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 4px;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Experience & project cards */
    .timeline-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 4px solid #3b82f6;
        border-radius: 10px;
        padding: 20px 24px;
        margin-bottom: 20px;
    }
    .tag-pill {
        display: inline-block;
        background: rgba(59, 130, 246, 0.1);
        color: #60a5fa;
        border: 1px solid rgba(59, 130, 246, 0.25);
        border-radius: 6px;
        padding: 2px 10px;
        font-size: 0.75rem;
        font-weight: 500;
        margin-right: 6px;
        margin-top: 6px;
    }

    /* Button adjustments */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)

FULL_NAME = "Mohamed Hisham Ibrahim"
ROLE_TITLE = "Data Analyst & Business Intelligence Specialist"
LOCATION = "Cairo, Egypt 🇪🇬"
PRIMARY_EMAIL = "mohamedhisha77@gmail.com"
PHONES = ["01062911800", "01115846343"]
LINKEDIN_URL = "https://www.linkedin.com/in/mohamed-hisham-ibrahim"
GITHUB_URL = "https://github.com/mohameddhisham"

with st.sidebar:
    st.markdown(f"## 📊 {FULL_NAME}")
    st.markdown(f"**{ROLE_TITLE}**")
    st.caption(f"📍 {LOCATION}")
    st.write("---")

    # Navigation menu
    selected_page = st.radio(
        "Explore Sections",
        [
            "Overview & Metrics",
            "Professional Experience",
            "Featured Projects",
            "Interactive Analytics Demo",
            "Technical Skills",
            "Education & Contact"
        ],
        index=0
    )

    st.write("---")
    st.markdown("### 🔗 Connect With Me")
    st.markdown(f"""
    - 🌐 [LinkedIn Profile]({LINKEDIN_URL})
    - 🐙 [GitHub Repositories]({GITHUB_URL})
    - ✉️ [{PRIMARY_EMAIL}](mailto:{PRIMARY_EMAIL})
    - 📞 `{PHONES[0]}` | `{PHONES[1]}`
    """)

    # Resume download simulation
    sample_cv_text = f"""MOHAMED HISHAM IBRAHIM - DATA ANALYST
Email: {PRIMARY_EMAIL} | Phone: {PHONES[0]}
Location: {LOCATION}
LinkedIn: {LINKEDIN_URL} | GitHub: {GITHUB_URL}

SUMMARY:
Data Analyst proficient in Python, SQL, PowerBI, Looker Studio, Tableau, DAX, and data warehousing.
Expert in designing and optimizing ETL processes and interactive dashboards.

EXPERIENCE:
- Data Analyst @ Mismar (Feb. 2026 - Present)
- Real Time Analyst @ Outsourcing skill (Sep. 2022 - Mar. 2026)

EDUCATION:
- Helwan University, Bachelor of Business Information Systems (BIS), GPA: 3.41 (Excellent)
"""
    st.download_button(
        label="📄 Download Resume (Text)",
        data=sample_cv_text,
        file_name="Mohamed_Hisham_Resume.txt",
        mime="text/plain",
        use_container_width=True
    )
    st.caption("Built with Python & Streamlit • Fast & Responsive")

if selected_page == "Overview & Metrics":
    st.markdown('<div class="hero-badge">DATA ANALYST PORTFOLIO</div>', unsafe_allow_html=True)
    st.title("Transforming Complex Raw Data into Actionable Business Value")
    
    st.write("""
    I am a results-driven **Data Analyst** specialized in **Python, SQL, Power BI, Looker Studio, Tableau, DAX**, 
    and **Modern Data Warehousing**. I bridge the gap between raw data collection and high-level strategic decisions 
    by developing robust ETL pipelines, high-performance dashboards, and automated workflows.
    """)

    # Key highlight metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">11M+</div>
            <div class="metric-label">Records Processed</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1,000+</div>
            <div class="metric-label">Dashboard Stakeholders</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">25%</div>
            <div class="metric-label">Processing Time Saved</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">100%</div>
            <div class="metric-label">ETL Data Integrity</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    
    # Core competencies overview
    st.subheader("💡 Core Competencies & Value Proposition")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🔄 ETL & Data Warehousing")
        st.write("Constructing end-to-end data pipelines, cleaning massive tables with Pandas, and querying enterprise data via Google BigQuery and MySQL.")
    with c2:
        st.markdown("#### 📊 BI & Interactive Visuals")
        st.write("Authoring executive reports and real-time operational views in Power BI, Looker Studio, Metabase, and Tableau with advanced DAX logic.")
    with c3:
        st.markdown("#### ⚡ Automation & Workflow")
        st.write("Eliminating repetitive manual data collection routines using Python scripting, advanced Excel macros, and Zapier cloud webhooks.")

elif selected_page == "Professional Experience":
    st.title("💼 Professional Experience")
    st.caption("A track record of streamlining workflows, enhancing data accessibility, and empowering stakeholders.")

    # Experience 1: Mismar
    st.markdown("""
    <div class="timeline-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; color:#38bdf8;">Data Analyst</h3>
            <span style="font-weight:600; color:#94a3b8;">Feb. 2026 – Present</span>
        </div>
        <h4 style="margin:4px 0 12px 0; color:#f1f5f9;">Mismar</h4>
        <ul style="color:#cbd5e1; line-height:1.7;">
            <li>Extract, clean, and aggregate multi-source data utilizing <b>MySQL</b> and <b>Google BigQuery</b> for high-volume operational analytics.</li>
            <li>Architect and support dynamic production dashboards in <b>Metabase, Looker Studio, and PowerBI</b> for leadership and product squads.</li>
            <li>Automate cross-platform data synchronization and recurring reporting workflows leveraging <b>Zapier</b> and custom webhooks.</li>
            <li>Execute deep exploratory data analysis (EDA) using <b>Python</b> and <b>Advanced Excel</b> to isolate behavioral patterns and revenue bottlenecks.</li>
            <li>Formulate analytical hypotheses, translating complex technical findings into digestible stakeholder presentations and strategic recommendations.</li>
        </ul>
        <div style="margin-top:12px;">
            <span class="tag-pill">Google BigQuery</span>
            <span class="tag-pill">MySQL</span>
            <span class="tag-pill">Power BI</span>
            <span class="tag-pill">Looker Studio</span>
            <span class="tag-pill">Metabase</span>
            <span class="tag-pill">Python</span>
            <span class="tag-pill">Zapier</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Experience 2: Outsourcing skill
    st.markdown("""
    <div class="timeline-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; color:#38bdf8;">Real Time Analyst</h3>
            <span style="font-weight:600; color:#94a3b8;">Sep. 2022 – Mar. 2026</span>
        </div>
        <h4 style="margin:4px 0 12px 0; color:#f1f5f9;">Outsourcing skill</h4>
        <ul style="color:#cbd5e1; line-height:1.7;">
            <li>Programmed Python and advanced spreadsheet automation suites to eradicate redundant manual logs, drastically raising team bandwidth.</li>
            <li>Monitored, analyzed, and audited disparate data points to extract high-impact insights that elevated call-center KPI compliance and SLA fulfillment.</li>
            <li>Collaborated with engineering and operational units to build scalable data visualization solutions reaching over <b>1,000+ daily active users</b>.</li>
            <li>Restructured underlying dimensional data models, delivering a measured <b>25% reduction in overall query and data processing latency</b>.</li>
            <li>Formulated stringent ETL hygiene checks, securing <b>100% data integrity</b> across downstream executive reports and audit databases.</li>
        </ul>
        <div style="margin-top:12px;">
            <span class="tag-pill">Python ETL</span>
            <span class="tag-pill">Data Modeling</span>
            <span class="tag-pill">Advanced Excel</span>
            <span class="tag-pill">SLA Optimization</span>
            <span class="tag-pill">Cross-functional BI</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_page == "Featured Projects":
    st.title("🚀 Featured Analytical Projects")
    st.write("Practical implementations highlighting big data ingestion, hygiene auditing, and automated pipelines.")

    p1, p2 = st.columns(2)

    with p1:
        st.markdown("""
        <div class="timeline-card" style="min-height: 380px;">
            <h3 style="color:#38bdf8; margin-top:0;">Automated Lead Filtration System</h3>
            <p style="color:#94a3b8; font-size:0.9rem;">Automated Ingestion & Algorithmic Cleaning Pipeline</p>
            <p style="color:#cbd5e1; line-height:1.6;">
                Engineered an intelligent filtering engine in Python using Pandas to ingest high-volume, volatile CSV lead datasets. 
                Constructed dynamic condition logic to screen lead dispositions against customizable blacklists and statuses, 
                eliminating invalid entries before CRM insertion.
            </p>
            <h5 style="color:#f8fafc; margin-bottom:6px;">Key Highlights:</h5>
            <ul style="color:#cbd5e1; font-size:0.9rem; padding-left:18px;">
                <li>Handled missing fields and corrupted text encodings automatically.</li>
                <li>Created flexible status matchers adaptable to varying vendor formats.</li>
                <li>Boosted lead processing throughput while curtailing CRM storage costs.</li>
            </ul>
            <div style="margin-top:14px;">
                <span class="tag-pill">Python</span>
                <span class="tag-pill">Pandas</span>
                <span class="tag-pill">ETL</span>
                <span class="tag-pill">Data Cleansing</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📂 View on GitHub", f"{GITHUB_URL}", use_container_width=True)

    with p2:
        st.markdown("""
        <div class="timeline-card" style="min-height: 380px;">
            <h3 style="color:#38bdf8; margin-top:0;">Big Data Quality & Duplicate Detection</h3>
            <p style="color:#94a3b8; font-size:0.9rem;">High-Volume Record Processing & Vendor Audit</p>
            <p style="color:#cbd5e1; line-height:1.6;">
                Conducted deep data quality investigations on a massive corpus exceeding <b>11 million customer records</b>. 
                Formulated chunked memory-efficient Python algorithms to parse records, exposing recurring vendor duplicate patterns 
                and saving valuable business budget.
            </p>
            <h5 style="color:#f8fafc; margin-bottom:6px;">Key Highlights:</h5>
            <ul style="color:#cbd5e1; font-size:0.9rem; padding-left:18px;">
                <li>Processed 11,000,000+ data rows with optimized Python batching.</li>
                <li>Uncovered systemic vendor redundancy and duplicate billing occurrences.</li>
                <li>Established recurring data health verification standards.</li>
            </ul>
            <div style="margin-top:14px;">
                <span class="tag-pill">Big Data</span>
                <span class="tag-pill">Python Performance</span>
                <span class="tag-pill">Data Auditing</span>
                <span class="tag-pill">SQL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📂 View on GitHub", f"{GITHUB_URL}", use_container_width=True)

elif selected_page == "Interactive Analytics Demo":
    st.title("📈 Interactive Live Analytics Playground")
    st.write("""
    Experience a live demo inspired by the **Lead Filtration System** and **Data Quality Analysis** projects.
    Adjust parameters below to see Python & Pandas process data on the fly!
    """)

    # Interactive controls
    ctrl_col1, ctrl_col2, ctrl_col3 = st.columns([1, 1, 1])
    with ctrl_col1:
        sample_size = st.slider("Select Record Batch Size", min_value=500, max_value=10000, value=2500, step=500)
    with ctrl_col2:
        duplicate_rate = st.slider("Inject Artificial Duplicates (%)", min_value=0, max_value=40, value=18, step=2)
    with ctrl_col3:
        filter_status = st.multiselect(
            "Filter Dispositions",
            ["Qualified", "Bad Number", "Do Not Call", "Disconnected", "Duplicate Vendor"],
            default=["Qualified"]
        )

    @st.cache_data
    def generate_lead_data(records_count, dup_pct):
        np.random.seed(42)
        channels = ["Paid Social", "Organic Search", "Direct", "Referral", "Cold Calling"]
        statuses = ["Qualified", "Bad Number", "Do Not Call", "Disconnected", "Duplicate Vendor"]
        
        data = {
            "Lead_ID": [f"LD-{10000 + i}" for i in range(records_count)],
            "Channel": np.random.choice(channels, size=records_count, p=[0.35, 0.25, 0.15, 0.15, 0.10]),
            "Disposition": np.random.choice(statuses, size=records_count, p=[0.45, 0.15, 0.10, 0.10, 0.20]),
            "Score": np.random.randint(20, 100, size=records_count),
            "Processing_Time_ms": np.random.normal(loc=12.5, scale=2.1, size=records_count).round(2)
        }
        df = pd.DataFrame(data)
        
        # Inoculate duplicates
        if dup_pct > 0:
            num_dups = int(records_count * (dup_pct / 100))
            if num_dups > 0:
                dup_indices = np.random.choice(df.index, size=num_dups, replace=False)
                df.loc[dup_indices, "Disposition"] = "Duplicate Vendor"
        return df

    raw_df = generate_lead_data(sample_size, duplicate_rate)

    # Filtering logic
    filtered_df = raw_df[raw_df["Disposition"].isin(filter_status)] if filter_status else raw_df

    # Quick metric ribbons
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Ingested", f"{len(raw_df):,}")
    m2.metric("Filtered Leads", f"{len(filtered_df):,}")
    m3.metric("Filtered Retention Rate", f"{(len(filtered_df)/len(raw_df)*100):.1f}%")
    m4.metric("Avg Ingestion Latency", f"{raw_df['Processing_Time_ms'].mean():.2f} ms")

    st.write("---")

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.subheader("📊 Lead Disposition Breakdown")
        status_counts = raw_df["Disposition"].value_counts().reset_index()
        status_counts.columns = ["Disposition", "Count"]
        fig_donut = px.pie(
            status_counts, 
            values="Count", 
            names="Disposition", 
            hole=0.45,
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        fig_donut.update_layout(margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_donut, use_container_width=True)

    with chart_col2:
        st.subheader("⚡ Lead Scoring by Acquisition Channel")
        fig_box = px.box(
            filtered_df if not filtered_df.empty else raw_df, 
            x="Channel", 
            y="Score", 
            color="Channel",
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        fig_box.update_layout(showlegend=False, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_box, use_container_width=True)

    # Data inspection table
    with st.expander("🔍 Inspect Filtered Records Batch"):
        st.dataframe(filtered_df.head(100), use_container_width=True)

elif selected_page == "Technical Skills":
    st.title("🛠️ Technical Skills & Tooling")
    st.caption("A balanced balance of query languages, BI suites, scripting, and business acumen.")

    sc1, sc2 = st.columns([1, 1])

    with sc1:
        st.subheader("Core Proficiencies")
        skills_data = {
            "Skill": [
                "SQL (MySQL, BigQuery)",
                "Power BI & DAX",
                "Python (Pandas, NumPy, Analysis)",
                "Looker Studio & Metabase",
                "Advanced Excel & Modeling",
                "Tableau",
                "ETL Pipeline Design",
                "Workflow Automation (Zapier)"
            ],
            "Proficiency": [95, 95, 90, 92, 95, 85, 90, 88]
        }
        skills_df = pd.DataFrame(skills_data)
        
        fig_bar = px.bar(
            skills_df.sort_values(by="Proficiency", ascending=True),
            x="Proficiency",
            y="Skill",
            orientation="h",
            color="Proficiency",
            color_continuous_scale="Blues",
            range_x=[0, 100],
            text="Proficiency"
        )
        fig_bar.update_traces(texttemplate="%{text}%", textposition="outside")
        fig_bar.update_layout(showlegend=False, height=420, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_bar, use_container_width=True)

    with sc2:
        st.subheader("Specialization Breakdown")
        radar_categories = ["Querying & SQL", "Data Visualization", "Python Scripting", "ETL & Modeling", "Stakeholder Comm.", "Business Analysis"]
        radar_values = [95, 92, 90, 90, 94, 92]

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=radar_values + [radar_values[0]],
            theta=radar_categories + [radar_categories[0]],
            fill='toself',
            fillcolor='rgba(59, 130, 246, 0.3)',
            line=dict(color='#3b82f6', width=2),
            name="Skill Radar"
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100])
            ),
            showlegend=False,
            height=420,
            margin=dict(l=30, r=30, t=20, b=20)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    # Soft skills & Methodologies
    st.write("---")
    st.subheader("🤝 Interpersonal & Operational Strengths")
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown("✅ **Data Storytelling**\nTranslating numbers to business narratives.")
    c2.markdown("✅ **Cross-Functional Teamwork**\nPartnered across Ops, Engineering, & Sales.")
    c3.markdown("✅ **Agile SLA Management**\nProven call center SLA monitoring.")
    c4.markdown("✅ **Problem Solving**\nDissecting complex duplicate & bottleneck trends.")

elif selected_page == "Education & Contact":
    st.title("🎓 Education & 📬 Get in Touch")

    col_edu, col_contact = st.columns([1, 1])

    with col_edu:
        st.subheader("Education")
        st.markdown("""
        <div class="timeline-card">
            <h4 style="color:#38bdf8; margin:0;">Bachelor of Business Information Systems (BIS)</h4>
            <p style="color:#f8fafc; font-weight:600; margin:4px 0;">Helwan University (2019 – 2023)</p>
            <p style="color:#10b981; font-weight:700; margin-bottom:8px;">GPA: 3.41 (Excellent)</p>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.6;">
                Focused on database design, information systems management, commercial software engineering, 
                and enterprise statistical analysis.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("Direct Contacts")
        st.markdown(f"""
        - 📧 **Email:** [{PRIMARY_EMAIL}](mailto:{PRIMARY_EMAIL})
        - 📱 **Phone 1:** `{PHONES[0]}`
        - 📱 **Phone 2:** `{PHONES[1]}`
        - 🌍 **Location:** {LOCATION}
        - 💼 **LinkedIn:** [linkedin.com/in/mohamed-hisham-ibrahim]({LINKEDIN_URL})
        - 🐙 **GitHub:** [github.com/mohameddhisham]({GITHUB_URL})
        """)

    with col_contact:
        st.subheader("Send a Message")
        with st.form("contact_form"):
            sender_name = st.text_input("Your Name / Organization", placeholder="e.g. Talent Acquisition / Engineering Lead")
            sender_email = st.text_input("Your Email", placeholder="name@company.com")
            message_subject = st.text_input("Subject", placeholder="Data Analyst Opportunity / Project Discussion")
            message_body = st.text_area("Message", placeholder="Write your message or inquiry here...", height=120)
            
            submitted = st.form_submit_button("✉️ Send Message", use_container_width=True)
            if submitted:
                if sender_name and sender_email and message_body:
                    st.success("Thank you! Your message has been received. I will reach out shortly.")
                else:
                    st.warning("Please fill out all required fields before submitting.")

    st.write("---")
    st.markdown("### 🚀 Connect to GitHub & Deploy to Streamlit Cloud")
    st.info(f"""
    **How to run and deploy this portfolio in 3 quick steps:**
    1. **Create a GitHub repo:** Create a repository named `data-analyst-portfolio` on your GitHub account (`{GITHUB_URL}`).
    2. **Push files:** Add this `app.py` and a `requirements.txt` containing:
       ```
       streamlit
       pandas
       numpy
       plotly
       ```
    3. **Deploy Free on Streamlit Cloud:** Go to [share.streamlit.io](https://share.streamlit.io), connect your GitHub account, choose your repository and branch, and your live portfolio will be online in seconds!
    """)
