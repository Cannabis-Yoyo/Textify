# # app.py (FINAL – STABLE – DEPLOYABLE, UTF-8 PDF)

# import os
# import math
# from datetime import datetime
# import streamlit as st
# from fpdf import FPDF
# from textify_core import Textify

# # -----------------------------
# # Streamlit Config
# # -----------------------------
# st.set_page_config(
#     page_title="Textify | Text Analysis Platform",
#     page_icon="📄",
#     layout="wide"
# )

# # -----------------------------
# # UI Styling
# # -----------------------------
# st.markdown("""
# <style>
# [data-testid="stAppViewContainer"] {
#     background-color: #F8F9FA;
#     border: 2px solid #0B3C5D;
#     border-radius: 12px;
#     padding: 24px;
# }
# .title-banner {
#     background-color: #0B3C5D;
#     color: white;
#     padding: 22px;
#     border-radius: 10px;
#     margin-bottom: 25px;
# }
# .section-header {
#     font-size: 22px;
#     font-weight: 600;
#     margin-top: 28px;
# }
# .card {
#     background-color: white;
#     padding: 20px;
#     border-radius: 8px;
#     margin-bottom: 18px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -----------------------------
# # Header
# # -----------------------------
# st.markdown("""
# <div class="title-banner">
# <h1>Textify – Summarization & Analysis Platform</h1>
# <p>Professional text intelligence</p>
# </div>
# """, unsafe_allow_html=True)

# # -----------------------------
# # Sidebar
# # -----------------------------
# st.sidebar.header("📥 Text Input")
# user_text = st.sidebar.text_area("Paste text here", height=280)

# max_length = st.sidebar.slider("Maximum Summary Length", 50, 500, 150)
# min_length = st.sidebar.slider("Minimum Summary Length", 25, 300, 50)

# # -----------------------------
# # PDF Generator (UTF-8 safe)
# # -----------------------------
# def generate_pdf(result):
#     pdf = FPDF()
#     pdf.add_page()
    
#     # Use DejaVu font to support Unicode
#     font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")
#     pdf.add_font('DejaVu', '', font_path, uni=True)
#     pdf.set_font("DejaVu", size=11)

#     def clean(text):
#         if not text:
#             return ""
#         return str(text)

#     pdf.cell(0, 10, "TEXTIFY ANALYSIS REPORT", ln=True)
#     pdf.ln(5)

#     pdf.multi_cell(0, 8, clean(result.get("summary", "")))
#     pdf.ln(4)

#     sentiment = result.get("sentiment", {})
#     pdf.cell(0, 8, f"Sentiment: {clean(sentiment.get('overall_sentiment',''))}", ln=True)
#     pdf.cell(0, 8, f"Confidence: {sentiment.get('confidence',0)*100:.1f}%", ln=True)

#     return pdf.output(dest="S").encode("utf-8")

# # -----------------------------
# # Analyze Button
# # -----------------------------
# if st.sidebar.button("🚀 Analyze Text"):
#     if not user_text.strip():
#         st.warning("Please enter text")
#     else:
#         with st.spinner("Processing..."):
#             result = Textify().process_text(user_text)

#         st.download_button(
#             "📄 Download Report",
#             generate_pdf(result),
#             "Textify_Report.pdf",
#             "application/pdf"
#         )

#         st.markdown('<div class="section-header">Executive Summary</div>', unsafe_allow_html=True)
#         st.markdown(f"<div class='card'>{result.get('summary','')}</div>", unsafe_allow_html=True)

#         st.markdown('<div class="section-header">Sentiment Analysis</div>', unsafe_allow_html=True)
#         st.markdown(f"<div class='card'>{result.get('sentiment','')}</div>", unsafe_allow_html=True)

#         st.success("Analysis completed successfully.")

# app.py (FINAL – STABLE – DEPLOYABLE, UTF-8 PDF)

import os
import math
import streamlit as st
from fpdf import FPDF
from textify_core import Textify

# -----------------------------
# Streamlit Config
# -----------------------------
st.set_page_config(
    page_title="Textify | Text Analysis Platform",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# UI Styling
# -----------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #F8F9FA;
    border: 2px solid #0B3C5D;
    border-radius: 12px;
    padding: 24px;
}
.title-banner {
    background-color: #0B3C5D;
    color: white;
    padding: 22px;
    border-radius: 10px;
    margin-bottom: 25px;
}
.section-header {
    font-size: 22px;
    font-weight: 600;
    color: #0B3C5D;
    margin-top: 28px;
    margin-bottom: 8px;
}
.card {
    background-color: #FFFFFF;
    color: #000000;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #DEE2E6;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.06);
    margin-bottom: 18px;
}
div.stDownloadButton > button {
    background-color: #1C7ED6;
    color: white;
    border-radius: 6px;
    padding: 10px 18px;
    font-weight: 600;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="title-banner">
<h1>Textify – Summarization & Analysis Platform</h1>
<p>Professional text intelligence for summaries, sentiment, trends, and insights</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("📥 Text Input")
user_text = st.sidebar.text_area(
    "Paste text here",
    height=280,
    placeholder="Paste your reports, emails, or articles here..."
)
max_length = st.sidebar.slider("Maximum Summary Length", 50, 500, 150)
min_length = st.sidebar.slider("Minimum Summary Length", 25, 300, 50)
# -----------------------------
# PDF Generator (Unicode-safe, NO bold font)
# -----------------------------
def generate_pdf(result):
    pdf = FPDF()
    pdf.add_page()

    font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=16)

    def clean(t):
        return str(t) if t else ""

    # Title
    pdf.cell(0, 10, "TEXTIFY ANALYSIS REPORT", ln=True)
    pdf.ln(6)

    # Executive Summary
    pdf.set_font("DejaVu", size=13)
    pdf.cell(0, 8, "Executive Summary", ln=True)
    pdf.set_font("DejaVu", size=11)
    pdf.multi_cell(0, 8, clean(result.get("summary", "")))
    pdf.ln(4)

    # Sentiment
    pdf.set_font("DejaVu", size=13)
    pdf.cell(0, 8, "Sentiment Analysis", ln=True)
    pdf.set_font("DejaVu", size=11)

    sentiment = result.get("sentiment", {})
    pdf.cell(0, 8, f"Overall Sentiment: {clean(sentiment.get('overall_sentiment'))}", ln=True)
    pdf.cell(0, 8, f"Confidence: {sentiment.get('confidence',0)*100:.1f}%", ln=True)
    pdf.ln(4)

    # Keywords
    pdf.set_font("DejaVu", size=13)
    pdf.cell(0, 8, "Key Topics & Trends", ln=True)
    pdf.set_font("DejaVu", size=11)

    keywords = result.get("keywords", [])
    if keywords:
        for k in keywords:
            pdf.cell(0, 8, f"- {clean(k)}", ln=True)
    else:
        pdf.cell(0, 8, "No keywords detected", ln=True)

    pdf.ln(4)

    # Insights
    pdf.set_font("DejaVu", size=13)
    pdf.cell(0, 8, "Actionable Insights", ln=True)
    pdf.set_font("DejaVu", size=11)

    insights = result.get("insights", [])
    if insights:
        for i in insights:
            pdf.multi_cell(0, 8, f"- {clean(i)}")
    else:
        pdf.cell(0, 8, "No actionable insights found", ln=True)

    return pdf.output(dest="S").encode("utf-8")

# -----------------------------
# Analyze Button
# -----------------------------
if st.sidebar.button("🚀 Analyze Text"):
    if not user_text.strip():
        st.warning("Please enter some text")
    else:
        with st.spinner("Processing..."):
            result = Textify().process_text(user_text)

        st.download_button(
            "📄 Download Report",
            generate_pdf(result),
            "Textify_Report.pdf",
            "application/pdf"
        )

        st.markdown('<div class="section-header">Executive Summary</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='card'>{result.get('summary','')}</div>", unsafe_allow_html=True)

        st.markdown('<div class="section-header">Sentiment Analysis</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='card'>{result.get('sentiment','')}</div>", unsafe_allow_html=True)

        st.success("Analysis completed successfully.")


