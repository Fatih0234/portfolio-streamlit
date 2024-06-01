from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
data_analyst_cert = str(current_dir / "assets" / "data-analyst-datacamp.png")
data_analyst_assoicate_cert = str(current_dir / "assets" / "data-analyst-associate-datacamp.png")
power_bi_cert = str(current_dir / "assets" / "powerbi-microsoft.png")
azure_cert = str(current_dir / "assets" / "azure-fundemantals-microsoft.png")
sql_cert = str(current_dir / "assets" / "sql-datacamp.png")

certifications = {
    "Data Analyst - DataCamp": {
        "image": data_analyst_cert,
        "description": "Issued May 2024 · Expires May 2026\nCredential ID: DA0020435722877",
        "skills": "**Skills:** Statistical Data Analysis · Exploratory Data Analysis · Data Visualization · Data Storytelling · Data Reporting · Data Management · Python Pandas · SQL",
        "url": "https://www.datacamp.com/certificate/DA0020435722877"
    },
    "Azure Fundamentals - Microsoft": {
        "image": azure_cert,
        "description": "Issued May 2024\nCredential ID: 1F632B20F4E61003",
        "skills": "**Skills:** Microsoft Azure · Cloud Applications · Cloud Computing · Cloud Storage · Cloud Security · Cloud Management",
        "url": "https://learn.microsoft.com/en-us/users/fatihkarahan-8457/credentials/1f632b20f4e61003?ref=https%3A%2F%2Fwww.linkedin.com%2F"
    },
    "Power BI Data Analyst Associate - Microsoft": {
        "image": power_bi_cert,
        "description": "Issued May 2024 · Expires May 2025\nCredential ID: 5A534D07A3944405",
        "skills": "**Skills:** Microsoft Power BI · Data Visualization · KPI Dashboards · Microsoft SQL Server · Data Modeling · Data Pipelines",
        "url": "https://learn.microsoft.com/en-us/users/fatihkarahan-8457/credentials/5a534d07a3944405?ref=https%3A%2F%2Fwww.linkedin.com%2F"
    },
    "Associate SQL - DataCamp": {
        "image": sql_cert,
        "description": "Issued Mar 2024 · Expires Mar 2026\nCredential ID: SQA0016933925509",
        "skills": "**Skills:** PostgreSQL · Databases · Data Modeling · Data Pipelines · Data Analysis · Data Warehousing",
        "url": "https://www.datacamp.com/certificate/SQA0016933925509"
    },
    "Data Analyst Associate - DataCamp": {
        "image": data_analyst_assoicate_cert,
        "description": "Issued Mar 2024 · Expires Mar 2026\nCredential ID: DAA0015004978126",
        "skills": "**Skills:** Data Visualization · Python Pandas · Statistical Data Analysis · Databases",
        "url": "https://www.datacamp.com/certificate/DAA0015004978126"
    },
}



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Fatih Karahan"
PAGE_ICON = ":wave:"
NAME = "Fatih Karahan"
DESCRIPTION = """
As a passionate data scientist and analyst, I thrive on creating innovative data-driven applications, such as a house predictor app that scrapes, automates, and predicts rent prices. My strong background in data analytics, coupled with my ability to build and deploy end-to-end solutions, aligns perfectly with my ambition to drive impactful insights and digital innovation in the business and economic sectors."""
EMAIL = "sekanti02@gmail.com"
SOCIAL_MEDIA = {
    "Medium": "https://medium.com/@sekanti02",
    "LinkedIn": "https://www.linkedin.com/in/fatih-karahan-717931193/",
    "GitHub": "https://github.com/Fatih0234",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 House Rent Price Predictor - Modeled with live data by webscraping Craiglist ads.": "https://housescraper-fatihkarahan.streamlit.app/",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy, Scrapy, Django, Flask), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Certifications")
st.write("---")
# Iterate over the certifications dictionary and display the details 
for cert in certifications.keys():
    details = certifications[cert]
    image_path = details["image"]
    image = Image.open(image_path)
    st.image(image, caption=cert, width=300)
    # Display the details of the certification
    st.write(f"**{cert}**")
    st.write(details["description"])
    st.write(details["skills"])
    st.write(f"[View Certificate]({details['url']})")
    st.write("---")