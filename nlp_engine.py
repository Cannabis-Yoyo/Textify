# nlp_engine.py (FINAL – TRANSFORMERS 4.38+ SAFE)

from transformers import pipeline

class NLPEngine:
    def __init__(self):
        # Sentiment analysis
        self.sentiment_model = pipeline(
            task="sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

        # ✅ FIXED: summarization task name
        self.summarizer = pipeline(
            task="text2text-generation",
            model="facebook/bart-large-cnn"
        )

    def summarize_text(self, text, max_length=150, min_length=50):
        result = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        return result[0]["generated_text"]

    def analyze_sentiment(self, text):
        sentences = [s for s in text.split(".") if s.strip()][:10]
        results = self.sentiment_model(sentences)

        score = sum(
            r["score"] if r["label"] == "POSITIVE" else -r["score"]
            for r in results
        ) / len(results)

        return {
            "overall_sentiment": "positive" if score >= 0 else "negative",
            "confidence": round(abs(score), 2)
        }
