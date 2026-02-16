# nlp_engine.py (TRULY NLTK-FREE – STREAMLIT SAFE)

from transformers import pipeline

class NLPEngine:
    def __init__(self):
        # Sentiment model
        self.sentiment_model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

        # Summarizer
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

    def summarize_text(self, text, max_length=150, min_length=50):
        result = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        return result[0]["summary_text"]

    def analyze_sentiment(self, text):
        # Transformers can handle long text directly
        result = self.sentiment_model(text[:512])

        label = result[0]["label"]
        score = result[0]["score"]

        return {
            "overall_sentiment": "positive" if label == "POSITIVE" else "negative",
            "confidence": round(score, 2)
        }
