from nlp_engine import NLPEngine
from trends import TrendAnalyzer
from insights import InsightExtractor

class Textify:
    def __init__(self):
        self.nlp = NLPEngine()
        self.trends = TrendAnalyzer()
        self.insights = InsightExtractor()

    def process_text(self, text):
        summary = self.nlp.summarize_text(text)
        sentiment = self.nlp.analyze_sentiment(text)
        keywords = self.trends.extract_keywords([text])
        insights = self.insights.generate_insights(summary, sentiment, keywords)

        return {
            "summary": summary,
            "sentiment": sentiment,
            "keywords": keywords,
            "insights": insights
        }


def get_user_input():
    print("\n📝 Enter your text below (type 'END' on a new line to finish):\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    return " ".join(lines)


if __name__ == "__main__":
    user_text = get_user_input()

    if not user_text.strip():
        print("❌ No text entered. Exiting.")
        exit()

    app = Textify()
    result = app.process_text(user_text)

    print("\n📌 SUMMARY:\n", result["summary"])
    print("\n📊 SENTIMENT:\n", result["sentiment"])
    print("\n📈 KEYWORDS:\n", result["keywords"])
    print("\n💡 INSIGHTS:")
    for insight in result["insights"]:
        print("-", insight)
