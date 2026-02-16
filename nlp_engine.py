# nlp_engine.py (FIXED FOR STREAMLIT + PYTHON 3.13)

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize.punkt import PunktSentenceTokenizer
from transformers import pipeline


class NLPEngine:
    def __init__(self):
        # Initialize sentiment analyzer
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

        # Sentence tokenizer (NO punkt_tab dependency)
        self.sentence_tokenizer = PunktSentenceTokenizer()

        # Summarization pipeline
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

    def summarize_text(self, text, max_length=150, min_length=50):
        summary = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        return summary[0]["summary_text"]

    def analyze_sentiment(self, text):
        # 🔥 FIX: NO sent_tokenize()
        sentences = self.sentence_tokenizer.tokenize(text)

        scores = [self.sentiment_analyzer.polarity_scores(s)["compound"] for s in sentences]
        avg_score = sum(scores) / len(scores) if scores else 0

        sentiment = "positive" if avg_score >= 0 else "negative"
        confidence = abs(avg_score)

        return {
            "overall_sentiment": sentiment,
            "confidence": round(confidence, 2)
        }
