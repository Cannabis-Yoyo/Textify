class InsightExtractor:
    def __init__(self):
        pass

    def generate_insights(self, summary, sentiment, keywords):
        insights = []

        insights.append(
            f"Primary sentiment detected: {sentiment['overall_sentiment']}"
        )

        if sentiment["overall_sentiment"] == "negative":
            insights.append("⚠️ Potential risk or dissatisfaction detected.")
        else:
            insights.append("✅ Content indicates positive or stable outlook.")

        insights.append(
            f"Key recurring themes: {', '.join(keywords[:5])}"
        )

        insights.append(
            "This summary highlights the most influential ideas for rapid decision-making."
        )

        return insights
