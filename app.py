import streamlit as st
from parser import extract_text_from_pdf
from agent import evaluate_candidate

# Streamlit Page Configuration
st.set_page_config(
    page_title="AI Recruitment Agent",
    page_icon="💼",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        padding-top: 1.5rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 6px;
        height: 3em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.title("💼 AI Recruitment Agent (Local TF-IDF Engine)")
st.write("Screen resumes locally using TF-IDF matching and keyword gap analysis—no API keys or external credits required.")

st.markdown("---")

# Layout: Two Columns for Inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Job Description")
    job_description = st.text_area(
        "Paste Job Description & Requirements",
        height=280,
        placeholder="Paste the target job role, required skills, and expectations here..."
    )

with col2:
    st.subheader("2. Candidate Resume")
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF format)",
        type=["pdf"],
        help="Upload the applicant's resume in PDF format."
    )
    
    resume_text = ""
    if uploaded_file is not None:
        try:
            # Extracts text using parser.py locally
            resume_text = extract_text_from_pdf(uploaded_file)
            if resume_text.strip():
                st.success(f"Successfully extracted text from `{uploaded_file.name}`")
                with st.expander("Preview Extracted Resume Text"):
                    st.text(resume_text[:1000] + ("..." if len(resume_text) > 1000 else ""))
            else:
                st.warning("The uploaded PDF appears to be empty or contains scanned images without selectable text.")
        except Exception as e:
            st.error(f"Error parsing PDF: {e}")

st.markdown("---")

# Execution Action
if st.button("🚀 Evaluate Candidate", type="primary"):
    if not job_description.strip():
        st.warning("Please enter a Job Description.")
    elif not resume_text.strip():
        st.warning("Please upload a valid candidate resume PDF.")
    else:
        with st.spinner("Processing local TF-IDF match analysis..."):
            # Runs local evaluation engine from agent.py
            report = evaluate_candidate(resume_text, job_description)
            
            # Render evaluation results
            st.markdown(report)

            # Extract draft email section to display in an editable input box
            if "#### Draft Email:" in report:
                st.markdown("---")
                st.subheader("📧 Communication Draft")
                email_content = report.split("#### Draft Email:")[-1].strip()
                st.text_area("Review or Edit Email Response:", value=email_content, height=180)