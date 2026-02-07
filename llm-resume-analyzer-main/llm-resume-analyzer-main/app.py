import streamlit as st
from resume_parser import extract_text
from skill_extractor import extract_skills
from recommender import recommend_jobs

st.set_page_config(page_title="Resume Analyzer & Career Recommender")
st.title("📄 Resume Analyzer & Career Recommender")

# -------- INPUT OPTIONS --------
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
resume_text = st.text_area(
    "Or paste resume text here",
    height=250,
    placeholder="Paste resume content if PDF is not available..."
)

if uploaded_file:
    resume_text = extract_text(uploaded_file)

if resume_text:
    st.subheader("📌 Resume Text Preview")
    st.write(resume_text[:1000])

    skills = extract_skills(resume_text)

    st.subheader("🛠 Extracted Skills")
    st.write(skills)

    st.subheader("🧠 Resume Analysis Summary")
    st.write(
        "The candidate demonstrates good alignment with the identified technical skills. "
        "Further improvement can be achieved by strengthening missing or advanced domain skills."
    )

    jobs = recommend_jobs(skills)

    st.subheader("💼 Recommended Job Roles")
    st.write(jobs)
