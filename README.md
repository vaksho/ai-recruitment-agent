# 💼 AI Recruitment & Resume Screening Agent

An automated candidate screening application built with **Python**, **Streamlit**, and **Scikit-Learn**. This tool evaluates candidate resumes against job descriptions locally using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## ✨ Key Features

- 📄 **PDF Resume Parsing:** Extracts text directly from uploaded candidate PDF resumes.
- 🎯 **TF-IDF Match Scoring:** Calculates mathematical relevance and match percentages between job requirements and applicants.
- 🔍 **Skill Gap Analysis:** Highlights top matching keywords and identifies missing skills.
- ✉️ **Automated Response Emails:** Generates customizable shortlist, hold, or rejection email templates based on candidate scores.
- 🔒 **100% Local & Free:** Operates completely on your local machine with zero external API calls or token costs.

---

## 🛠️ Tech Stack

- **UI Framework:** Streamlit
- **NLP & Analytics:** Scikit-Learn (`TfidfVectorizer`, `cosine_similarity`)
- **PDF Extraction:** PyPDF (`pypdf`)
- **Language:** Python 3.10+

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/vaksho/ai-recruitment-agent.git](https://github.com/vaksho/ai-recruitment-agent.git)
   cd ai-recruitment-agent
