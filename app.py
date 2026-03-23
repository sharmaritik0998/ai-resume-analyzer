import streamlit as st
import matplotlib.pyplot as plt

from parser import extract_text_from_pdf
from skills import load_skills, extract_skills
from analyzer import calculate_score
from insights import generate_suggestions
from role_detector import detect_role

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# Title
st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:700;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">AI Resume Analyzer</p>', unsafe_allow_html=True)

# Inputs
uploaded_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:

    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Load + extract skills
    skills_list = load_skills()
    resume_skills = extract_skills(resume_text, skills_list)
    jd_skills = extract_skills(job_desc.lower(), skills_list)

    # Score
    score = calculate_score(resume_text, job_desc)

    # Role detection
    role = detect_role(job_desc)

    # Skill comparison
    missing_skills = list(set(jd_skills) - set(resume_skills))
    matched_skills = list(set(resume_skills) & set(jd_skills))

    # Suggestions
    suggestions = generate_suggestions(missing_skills, role)

    # SECTION
    st.markdown("## Match Analysis")

    col1, col2, col3 = st.columns(3)
    col1.metric("Match Score", f"{score}%")
    col2.metric("Skills Found", len(resume_skills))
    col3.metric("Missing Skills", len(missing_skills))

    st.progress(int(score))

    if score > 70:
        st.success("Strong match! You're a great fit.")
    elif score > 40:
        st.warning("Moderate match. Improve some areas.")
    else:
        st.error("Low match. Needs improvement.")

    st.markdown(f"### Detected Role: {role}")

    st.divider()

    # SKILLS
    st.markdown("## Skill Breakdown")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Matched Skills")
        st.write(matched_skills)

    with col2:
        st.error("Missing Skills")
        st.write(missing_skills)

    # PIE CHART
    st.markdown("## Skill Distribution")

    labels = ['Matched', 'Missing']
    values = [len(matched_skills), len(missing_skills)]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)

    st.divider()

    # SUGGESTIONS
    st.markdown("## Suggestions")

    if suggestions:
        for s in suggestions:
            st.success(s)
    else:
        st.info("Your resume looks strong!")