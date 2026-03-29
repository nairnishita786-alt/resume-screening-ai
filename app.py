import streamlit as st # pyright: ignore[reportMissingImports]
from resume_parser import extract_resume_text
from model import clean_text, get_similarity
from skills import extract_skills

st.title("Smart Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_resume_text("temp.pdf")
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_desc)

    score = get_similarity(resume_clean, job_clean)
    skills = extract_skills(resume_clean)

    st.subheader("Match Score:")
    st.write(round(score * 100, 2), "%")

    st.subheader("Skills Found:")
    st.write(skills)
