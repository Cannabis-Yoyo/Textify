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
from datetime import datetime
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
/* Page Container */
[data-testid="stAppViewContainer"] {
    background-color: #F8F9FA;
    border: 2px solid #0B3C5D;
    border-radius: 12px;
    padding: 24px;
}

/* Title Banner */
.title-banner {
    background-color: #0B3C5D;
    color: white;
    padding: 22px;
    border-radius: 10px;
    margin-bottom: 25px;
}

/* Section Header */
.section-header {
    font-size: 22px;
    font-weight: 600;
    color: #0B3C5D;
    margin-top: 28px;
    margin-bottom: 8px;
}

/* Card */
.card {
    background-color: #FFFFFF;
    color: #000000;  /* Ensure text is visible */
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #DEE2E6;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.06);
    margin-bottom: 18px;
}

/* Download Button */
div.stDownloadButton > button {
    background-color: #1C7ED6;
    color: white;
    border-radius: 6px;
    padding: 10px 18px;
    font-weight: 600;
    border: none;
    transition: all 0.25s ease-in-out;
}
div.stDownloadButton > button:hover {
    background-color: #1864AB;
    transform: scale(1.03);
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
# PDF Generator (UTF-8 safe)
# -----------------------------
def generate_pdf(result):
    pdf = FPDF()
    pdf.add_page()
    
    # DejaVu font for Unicode support
    font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.set_font("DejaVu", size=11)

    def clean(text):
        return str(text) if text else ""

    # Header
    pdf.set_font("DejaVu", "B", 16)
    pdf.cell(0, 10, "TEXTIFY ANALYSIS REPORT", ln=True)
    pdf.ln(5)

    # Executive Summary
    pdf.set_font("DejaVu", "B", 13)
    pdf.cell(0, 8, "Executive Summary", ln=True)
    pdf.set_font("DejaVu", size=11)
    pdf.multi_cell(0, 8, clean(result.get("summary", "")))
    pdf.ln(4)

    # Sentiment Analysis
    pdf.set_font("DejaVu", "B", 13)
    pdf.cell(0, 8, "Sentiment Analysis", ln=True)
    pdf.set_font("DejaVu", size=11)
    sentiment = result.get("sentiment", {})
    pdf.cell(0, 8, f"Overall Sentiment: {clean(sentiment.get('overall_sentiment',''))}", ln=True)
    pdf.cell(0, 8, f"Confidence: {sentiment.get('confidence',0)*100:.1f}%", ln=True)
    pdf.ln(4)

    # Key Topics & Trends
    pdf.set_font("DejaVu", "B", 13)
    pdf.cell(0, 8, "Key Topics & Trends", ln=True)
    pdf.set_font("DejaVu", size=11)
    keywords = result.get("keywords", [])
    if keywords:
        mid = math.ceil(len(keywords)/2)
        for i in range(mid):
            left = keywords[i]
            right = keywords[i+mid] if i+mid < len(keywords) else ""
            pdf.cell(90,8,f"- {clean(left)}")
            pdf.cell(0,8,f"- {clean(right)}", ln=True)
    else:
        pdf.cell(0,8,"No keywords detected", ln=True)
    pdf.ln(4)

    # Actionable Insights
    pdf.set_font("DejaVu", "B", 13)
    pdf.cell(0, 8, "Actionable Insights", ln=True)
    pdf.set_font("DejaVu", size=11)
    insights = result.get("insights", [])
    if insights:
        for ins in insights:
            pdf.multi_cell(0,8,clean(f"- {ins}"))
    else:
        pdf.cell(0,8,"No actionable insights found", ln=True)

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

        # Download PDF
        st.download_button(
            "📄 Download Report",
            generate_pdf(result),
            "Textify_Report.pdf",
            "application/pdf"
        )

        # Executive Summary
        st.markdown('<div class="section-header">Executive Summary</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='card'>{result.get('summary','')}</div>", unsafe_allow_html=True)

        # Sentiment Analysis
        sentiment = result.get("sentiment", {})
        conf = sentiment.get("confidence",0)*100
        color_sent = "#008000" if sentiment.get("overall_sentiment","")=="positive" else "#C00000"
        color_conf = "#C00000" if conf<=40 else "#FF8C00" if 50<=conf<=60 else "#008000"
        st.markdown('<div class="section-header">Sentiment Analysis</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class='card'>
                <p><b>Overall Sentiment:</b> <span style="color:{color_sent}; font-weight:bold;">{sentiment.get('overall_sentiment','').capitalize()}</span></p>
                <p><b>Confidence Level:</b> <span style="color:{color_conf}; font-weight:bold;">{conf:.1f}%</span></p>
            </div>
        """, unsafe_allow_html=True)

        # Key Topics & Trends
        st.markdown('<div class="section-header">Key Topics & Trends</div>', unsafe_allow_html=True)
        keywords = result.get("keywords", [])
        if keywords:
            mid = math.ceil(len(keywords)/2)
            left, right = keywords[:mid], keywords[mid:]
            html_keywords = "<div class='card'><div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'><ul>"
            for i in left: html_keywords += f"<li>{i}</li>"
            html_keywords += "</ul><ul>"
            for i in right: html_keywords += f"<li>{i}</li>"
            html_keywords += "</ul></div></div>"
            st.markdown(html_keywords, unsafe_allow_html=True)
        else:
            st.markdown("<div class='card'>No keywords detected</div>", unsafe_allow_html=True)

        # Actionable Insights
        st.markdown('<div class="section-header">Actionable Insights</div>', unsafe_allow_html=True)
        insights = result.get("insights", [])
        if insights:
            html_insights = "<div class='card'><ul>"
            for ins in insights: html_insights += f"<li>{ins}</li>"
            html_insights += "</ul></div>"
            st.markdown(html_insights, unsafe_allow_html=True)
        else:
            st.markdown("<div class='card'>No actionable insights found</div>", unsafe_allow_html=True)

        st.success("Analysis completed successfully.")
