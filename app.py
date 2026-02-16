import streamlit as st
from textify import Textify
from fpdf import FPDF
from datetime import datetime
import math
import nltk

# Download NLTK resources if not already present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)
# -------------------------------------------------
# App Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Textify | Text Analysis Platform",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------
# Global Styling
# -------------------------------------------------
st.markdown("""
<style>
/* Page Border */
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
    padding: 22px 26px;
    border-radius: 10px;
    border-left: 8px solid #1C7ED6;
    margin-bottom: 25px;
}
.title-banner h1 { margin:0; font-size:34px; }
.title-banner p { margin-top:6px; font-size:15px; opacity:0.9; }

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

# -------------------------------------------------
# Title
# -------------------------------------------------
st.markdown("""
<div class="title-banner">
    <h1>Textify – Summarization & Analysis Platform</h1>
    <p>Professional text intelligence for summaries, sentiment, trends, and insights</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar Input
# -------------------------------------------------
st.sidebar.header("📥 Text Input")
user_text = st.sidebar.text_area(
    "Paste text for analysis:",
    height=280,
    placeholder="Paste reports, articles, emails, or documents here..."
)
max_length = st.sidebar.slider("Maximum Summary Length", 50, 500, 150)
min_length = st.sidebar.slider("Minimum Summary Length", 25, 300, 50)

# -------------------------------------------------
# PDF Generator
# -------------------------------------------------
def generate_invoice_pdf(result):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    def clean(t): return t.encode("latin-1", "ignore").decode("latin-1")

    # Header
    pdf.set_fill_color(11,60,93)
    pdf.set_text_color(255,255,255)
    pdf.set_font("Helvetica","B",18)
    pdf.cell(0,14,"TEXTIFY ANALYSIS REPORT",ln=True,align="C",fill=True)

    pdf.ln(6)
    pdf.set_text_color(0,0,0)
    pdf.set_font("Helvetica",size=10)
    pdf.cell(0,8,f"Generated On: {datetime.now().strftime('%d %b %Y, %H:%M')}",ln=True)

    # Helper to make sections
    def section(title):
        pdf.ln(6)
        pdf.set_font("Helvetica","B",13)
        pdf.set_text_color(11,60,93)
        pdf.cell(0,10,title,ln=True)
        pdf.set_text_color(0,0,0)

    # Executive Summary
    section("Executive Summary")
    pdf.set_font("Helvetica",size=11)
    pdf.multi_cell(0,8,clean(result["summary"]))

    # Sentiment Analysis
    section("Sentiment Analysis")
    s = result["sentiment"]
    conf_pct = s["confidence"]*100
    pdf.cell(60,8,"Overall Sentiment:")
    if s["overall_sentiment"]=="positive": pdf.set_text_color(0,140,0)
    else: pdf.set_text_color(180,0,0)
    pdf.cell(0,8,s["overall_sentiment"].capitalize(),ln=True)
    pdf.set_text_color(0,0,0)
    pdf.cell(60,8,"Confidence Level:")
    if conf_pct <= 40: pdf.set_text_color(180,0,0)
    elif 50<=conf_pct<=60: pdf.set_text_color(255,140,0)
    else: pdf.set_text_color(0,140,0)
    pdf.cell(0,8,f"{conf_pct:.1f}%",ln=True)
    pdf.set_text_color(0,0,0)

    # Key Topics & Trends
    section("Key Topics & Trends")
    keywords = result.get("keywords", [])
    pdf.set_font("Helvetica", size=11)  # same font as Executive Summary
    if keywords:
        mid = math.ceil(len(keywords)/2)
        for i in range(mid):
            left = keywords[i]
            right = keywords[i+mid] if i+mid < len(keywords) else ""
            pdf.cell(90,8,f"- {clean(left)}")
            pdf.cell(0,8,f"- {clean(right)}",ln=True)
    else:
        pdf.cell(0,8,"No keywords detected",ln=True)

    # Actionable Insights
    section("Actionable Insights")
    insights = result.get("insights", [])
    pdf.set_font("Helvetica", size=11)  # same font as Executive Summary
    if insights:
        for ins in insights:
            pdf.multi_cell(0,8,clean(f"- {ins}"))
    else:
        pdf.cell(0,8,"No actionable insights found",ln=True)

    return pdf.output(dest="S").encode("latin-1")

# -------------------------------------------------
# Analyze Button
# -------------------------------------------------
if st.sidebar.button("🚀 Analyze Text"):
    if not user_text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Processing text..."):
            result = Textify().process_text(user_text)

        # Header + Download Button
        col1,col2 = st.columns([7,2])
        with col1:
            st.markdown('<div class="section-header">Analysis Results</div>', unsafe_allow_html=True)
        with col2:
            st.download_button(
                "📄 Download Report",
                data=generate_invoice_pdf(result),
                file_name="Textify_Analysis_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        # Executive Summary
        st.markdown('<div class="section-header">Executive Summary</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card">{result["summary"]}</div>', unsafe_allow_html=True)

        # Sentiment Analysis
        s = result["sentiment"]
        conf = s["confidence"]*100
        color_sent = "#008000" if s["overall_sentiment"]=="positive" else "#C00000"
        color_conf = "#C00000" if conf<=40 else "#FF8C00" if 50<=conf<=60 else "#008000"
        st.markdown('<div class="section-header">Sentiment Analysis</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="card">
                <p><b>Overall Sentiment:</b> <span style="color:{color_sent}; font-weight:bold;">{s['overall_sentiment'].capitalize()}</span></p>
                <p><b>Confidence Level:</b> <span style="color:{color_conf}; font-weight:bold;">{conf:.1f}%</span></p>
            </div>
        """, unsafe_allow_html=True)

        # Key Topics & Trends
        st.markdown('<div class="section-header">Key Topics & Trends</div>', unsafe_allow_html=True)
        k = result.get("keywords", [])
        if k:
            mid = math.ceil(len(k)/2)
            left, right = k[:mid], k[mid:]
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


