import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mohamed Hisham | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & Colors (CSS)
st.markdown("""
    <style>
    /* Main Background & Font styling */
    .main {
        background-color: #F8FAFC;
    }
    
    /* Headers */
    .main-header {
        font-size: 2.8rem;
        color: #0F172A;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.3rem;
        color: #0284C7;
        font-weight: 600;
        margin-bottom: 20px;
    }
    
    /* Section Headers */
    h2 {
        color: #1E3A8A !important;
        border-bottom: 2px solid #E2E8F0;
        padding-bottom: 8px;
        margin-top: 30px !important;
    }

    /* Cards styling */
    .card {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border-left: 5px solid #0284C7;
    }
    
    .skill-box {
        background-color: #EFF6FF;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
        color: #1E40AF;
        border: 1px solid #BFDBFE;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    # Adding a professional profile image placeholder (can be replaced with your actual image URL later)
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300&auto=format&fit=crop&q=80", caption="Mohamed Hisham", use_container_width=True)
    
    st.markdown("<h2 style='text-align: center; margin-top: 0px !important; font-size: 1.5rem;'>Mohamed Hisham</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #0284C7; font-weight: bold;'>Data Analyst</p>", unsafe_allow_html=True)
    st.markdown("📍 Cairo, Egypt")
    
    st.divider()
    st.markdown("### 📞 Quick Contact")
    st.markdown("📧 **Email:** [mohamedhisha77@gmail.com](mailto:mohamedhisha77@gmail.com)")
    st.markdown("📱 **Phone:** 01062911800")
    st.markdown("🔗 **[LinkedIn Profile](https://linkedin.com/in/mohamed-hisham-ibrahim)**")
    st.markdown("💻 **[GitHub Profile](https://github.com/mohameddhisham)**")

# --- Main Content ---
st.markdown('<p class="main-header">Hi, I\'m Mohamed Hisham 👋</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Data Analyst | Driving Strategic Business Decisions through Data</p>', unsafe_allow_html=True)

# About Me Box
st.markdown("""
<div class="card" style="border-left-color: #10B981;">
    <h3 style="margin-top:0; color: #065F46;">About Me</h3>
    <p style="font-size: 1.1rem; color: #334155;">
    I am a Data Analyst, proficient in Python, SQL, PowerBI, Tableau, DAX, and data warehousing, driving strategic business decisions. 
    Expert in designing and optimizing ETL processes and interactive dashboards, transforming complex data into clear, actionable insights[cite: 1].
    </p>
</div>
""", unsafe_allow_html=True)

# --- Experience Section ---
st.markdown("## 💼 Professional Experience")

# Job 1
st.markdown("""
<div class="card">
    <h3 style="color: #1E3A8A; margin-top:0;">Data Analyst | <span style="color: #0284C7;">Mismar</span></h3>
    <p style="color: #64748B; font-weight: 500;">Feb. 2026 - Present[cite: 1]</p>
    <ul>
        <li>Extract and analyze data using MySQL and Google BigQuery[cite: 1].</li>
        <li>Build and maintain dashboards using Metabase[cite: 1].</li>
        <li>Automate workflows and reporting processes using Zapier[cite: 1].</li>
        <li>Perform data analysis using Python and advanced Excel[cite: 1].</li>
        <li>Identify trends, patterns, and performance gaps, translating business requirements into clear analytical reports for stakeholders[cite: 1].</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Job 2
st.markdown("""
<div class="card">
    <h3 style="color: #1E3A8A; margin-top:0;">Real Time Analyst | <span style="color: #0284C7;">Outsourcing skill</span></h3>
    <p style="color: #64748B; font-weight: 500;">Sep. 2022 - Mar. 2026[cite: 1]</p>
    <ul>
        <li>Streamlined repetitive data collection tasks using Python and Excel to increase team efficiency[cite: 1].</li>
        <li>Analyzed data from various sources to extract insights and improve call center performance metrics[cite: 1].</li>
        <li>Collaborated with cross-functional teams to design data visualization solutions reaching 1000+ users[cite: 1].</li>
        <li>Developed and maintained complex data models, resulting in a <strong>25% reduction in data processing time</strong>[cite: 1].</li>
        <li>Performed ETL processes to clean and structure raw data, ensuring 100% data integrity for downstream reporting[cite: 1].</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- Projects Section ---
st.markdown("## 🚀 Featured Projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card" style="border-left-color: #8B5CF6; height: 100%;">
        <h3 style="color: #6D28D9; margin-top:0;">Automated Lead Filtration System</h3>
        <p><strong>Tools:</strong> Python, Pandas, CSV Datasets</p>
        <p>Implemented Python's Pandas library to process large lead datasets, handling missing values, and built a flexible filtering mechanism to discard unwanted lead statuses based on predefined rules[cite: 1].</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="border-left-color: #8B5CF6; height: 100%;">
        <h3 style="color: #6D28D9; margin-top:0;">Data Quality Analysis</h3>
        <p><strong>Tools:</strong> Python, Data Cleaning</p>
        <p>Successfully processed <strong>11 million records</strong> using efficient data manipulation to uncover consistent patterns of duplicate data sent by vendors and ensure robust data integrity[cite: 1].</p>
    </div>
    """, unsafe_allow_html=True)

# --- Skills Section ---
st.markdown("## 🛠️ Technical Skills")
s_col1, s_col2, s_col3, s_col4 = st.columns(4)

with s_col1:
    st.markdown('<div class="skill-box">🐍 Python & SQL<br><span style="font-size:0.85rem; color:#475569;">Pandas, MySQL, BigQuery</span></div>', unsafe_allow_html=True)
with s_col2:
    st.markdown('<div class="skill-box">📈 BI & Visualization<br><span style="font-size:0.85rem; color:#475569;">Power BI, Tableau, Metabase</span></div>', unsafe_allow_html=True)
with s_col3:
    st.markdown('<div class="skill-box">⚙️ Data Engineering<br><span style="font-size:0.85rem; color:#475569;">ETL, Zapier, Data Modeling</span></div>', unsafe_allow_html=True)
with s_col4:
    st.markdown('<div class="skill-box">📊 Tools & Soft Skills<br><span style="font-size:0.85rem; color:#475569;">Advanced Excel, Git, Git Workflow</span></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Education Section ---
st.markdown("## 🎓 Education")
st.markdown("""
<div class="card" style="border-left-color: #F59E0B;">
    <h3 style="color: #B45309; margin-top:0;">Bachelor of Business Information System</h3>
    <p style="margin-bottom: 5px;"><strong>Helwan University</strong> (2019 - 2023)[cite: 1]</p>
    <p style="color: #475569;"><strong>GPA:</strong> 3.41 (Excellent)[cite: 1]</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748B;'>© 2026 Mohamed Hisham | Built with Python & Streamlit 🚀</p>", unsafe_allow_html=True)
