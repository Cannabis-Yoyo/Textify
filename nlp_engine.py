# nlp_engine.py (FINAL – NO NLTK – STREAMLIT SAFE)

from transformers import pipeline
from nltk.tokenize.punkt import PunktSentenceTokenizer


class NLPEngine:
    def __init__(self):
        # Sentence tokenizer (NO punkt_tab)
        self.sentence_tokenizer = PunktSentenceTokenizer()

        # Sentiment model (NO vader)
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
        sentences = self.sentence_tokenizer.tokenize(text)
        results = self.sentiment_model(sentences[:10])  # cap for speed

        score = sum(
            r["score"] if r["label"] == "POSITIVE" else -r["score"]
            for r in results
        ) / len(results)

        return {
            "overall_sentiment": "positive" if score >= 0 else "negative",
            "confidence": round(abs(score), 2)
        }
