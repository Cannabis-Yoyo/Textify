# textify_core.py

from nlp_engine import NLPEngine
from trends import TrendAnalyzer
from insights import InsightExtractor

class Textify:
    def __init__(self):
        self.nlp = NLPEngine()
        self.trends = TrendAnalyzer()
        self.insights = InsightExtractor()

    def process_text(self, text, max_length=150, min_length=50):
        summary = self.nlp.summarize_text(
            text,
            max_length=max_length,
            min_length=min_length
        )

        sentiment = self.nlp.analyze_sentiment(text)
        keywords = self.trends.extract_keywords([text])
        insights = self.insights.generate_insights(summary, sentiment, keywords)

        return {
            "summary": summary,
            "sentiment": sentiment,
            "keywords": keywords,
            "insights": insights
        }
