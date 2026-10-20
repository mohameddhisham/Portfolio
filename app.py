import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mohamed Hisham | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (CSS)
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 700;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4B5563;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/data-configuration.png", width=80)
    st.markdown("### Mohamed Hisham")
    st.markdown("**Data Analyst**")
    st.markdown("📍 Cairo, Egypt")
    
    st.divider()
    st.markdown("### 📞 Contact & Links")
    st.markdown("📧 [mohamedhisha77@gmail.com](mailto:mohamedhisha77@gmail.com)")
    st.markdown("📞 01062911800 / 01115846343")
    st.markdown("🔗 [LinkedIn Profile](https://linkedin.com/in/mohamed-hisham-ibrahim)")
    st.markdown("💻 [GitHub Profile](https://github.com/mohameddhisham)")

# --- Main Content ---
# Hero Section
st.markdown('<p class="main-header">Hi, I\'m Mohamed Hisham 👋</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Data Analyst | Driving Strategic Business Decisions through Data</p>', unsafe_allow_html=True)

st.write("""
I am a Data Analyst, proficient in Python, SQL, PowerBI, Tableau, DAX, and data warehousing, driving strategic business decisions. 
Expert in designing and optimizing ETL processes and interactive dashboards, transforming complex data into clear, actionable insights[cite: 1].
""")

st.divider()

# --- Experience Section ---
st.markdown("## 💼 Professional Experience")

# Job 1
st.markdown("### **Data Analyst** | **Mismar**")
st.markdown("*Feb. 2026 - Present*[cite: 1]")
st.markdown("""
- Extract and analyze data using MySQL and Google BigQuery[cite: 1].
- Build and maintain dashboards using Metabase[cite: 1].
- Automate workflows and reporting processes using Zapier[cite: 1].
- Perform data analysis using Python and advanced Excel[cite: 1].
- Identify trends, patterns, and performance gaps, translating business requirements into clear analytical reports for stakeholders[cite: 1].
""")

# Job 2
st.markdown("### **Real Time Analyst** | **Outsourcing skill**")
st.markdown("*Sep. 2022 - Mar. 2026*[cite: 1]")
st.markdown("""
- Streamlined repetitive data collection tasks using Python and Excel to increase team efficiency[cite: 1].
- Analyzed data from various sources to extract insights and improve call center performance metrics[cite: 1].
- Collaborated with cross-functional teams to design data visualization solutions reaching 1000+ users[cite: 1].
- Developed and maintained complex data models, resulting in a **25% reduction in data processing time**[cite: 1].
- Performed ETL processes to clean and structure raw data, ensuring 100% data integrity for downstream reporting[cite: 1].
""")

st.divider()

# --- Projects Section ---
st.markdown("## 🚀 Featured Projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 1. Automated Lead Filtration System")
    st.write("""
    - **Data Ingestion & Cleaning:** Implemented Python's Pandas library to process large CSV lead datasets, handling missing values and inconsistencies[cite: 1].
    - **Flexible Filtering:** Created a mechanism to filter out unwanted statuses by comparing lead dispositions against a predefined list using conditional statements[cite: 1].
    """)

with col2:
    st.markdown("### 2. Data Quality Analysis")
    st.write("""
    - **Massive Dataset Processing:** Successfully processed **11 million records** using Python's efficient data manipulation capabilities[cite: 1].
    - **Duplicate Detection:** Employed advanced filtering and cleaning techniques to uncover consistent patterns of duplicate data sent by vendors[cite: 1].
    """)

st.divider()

# --- Skills Section ---
st.markdown("## 🛠️ Technical Skills")
skills_col1, skills_col2, skills_col3, skills_col4 = st.columns(4)

with skills_col1:
    st.markdown("**Programming & Querying**")
    st.badge = st.markdown("- Python (Pandas)\n- SQL / MySQL\n- Google BigQuery")

with skills_col2:
    st.markdown("**Visualization & BI**")
    st.markdown("- Power BI\n- Tableau\n- Metabase\n- DAX")

with skills_col3:
    st.markdown("**Data Engineering**")
    st.markdown("- ETL Processes\n- Data Warehousing\n- Zapier Automation")

with skills_col4:
    st.markdown("**Tools & Soft Skills**")
    st.markdown("- Advanced Excel\n- Git / GitHub\n- Communication\n- Time Management")

st.divider()

# --- Education Section ---
st.markdown("## 🎓 Education")
st.markdown("**Bachelor of Business Information System** | **Helwan University** *(2019-2023)*[cite: 1]")
st.markdown("- **GPA:** 3.41 (Excellent)[cite: 1]")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Mohamed Hisham | Built with Streamlit & Python</p>", unsafe_allow_html=True)
