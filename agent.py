import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_candidate(resume_text, job_description):
    if not resume_text.strip() or not job_description.strip():
        return "Error: Empty input provided."

    # 1. Calculate Similarity Score using TF-IDF (Cosine Similarity)
    documents = [job_description, resume_text]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    match_percentage = round(similarity_score * 100, 2)

    # 2. Extract Keywords & Missing Skills
    words_jd = set(re.findall(r'\b[a-zA-Z]{3,}\b', job_description.lower()))
    words_resume = set(re.findall(r'\b[a-zA-Z]{3,}\b', resume_text.lower()))
    
    # Filter common noise words
    stopwords = {"and", "the", "for", "with", "that", "this", "from", "you", "are", "have", "will", "your", "must", "with", "work"}
    jd_keywords = words_jd - stopwords
    resume_keywords = words_resume - stopwords

    matched_skills = list(jd_keywords.intersection(resume_keywords))
    missing_skills = list(jd_keywords - resume_keywords)

    # 3. Determine Recommendation
    if match_percentage >= 50:
        recommendation = "Shortlist"
        status_color = "🟢"
        email_draft = (
            "Dear Candidate,\n\n"
            "We reviewed your application and are excited to invite you for an interview. "
            "Your background aligns well with our requirements.\n\n"
            "Best regards,\nRecruitment Team"
        )
    elif match_percentage >= 30:
        recommendation = "Hold / Review Manually"
        status_color = "🟡"
        email_draft = (
            "Dear Candidate,\n\n"
            "Thank you for your application. We are currently reviewing all applicants "
            "and will update you shortly.\n\n"
            "Best regards,\nRecruitment Team"
        )
    else:
        recommendation = "Reject"
        status_color = "🔴"
        email_draft = (
            "Dear Candidate,\n\n"
            "Thank you for applying. Although your experience is impressive, we have decided "
            "to proceed with candidates whose skills more closely match our needs.\n\n"
            "Best regards,\nRecruitment Team"
        )

    # 4. Construct Final Report Output
    report = f"""
    ### Evaluation Results

    **Match Score:** {match_percentage}%
    **Recommendation:** {status_color} {recommendation}

    #### Key Strengths & Matched Keywords:
    {", ".join(matched_skills[:15]) if matched_skills else "No major keyword matches found."}

    #### Missing Skills / Gaps:
    {", ".join(missing_skills[:15]) if missing_skills else "No significant gaps identified."}

    ---
    #### Draft Email:
    """
    return report