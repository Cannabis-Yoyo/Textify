# nlp_engine.py (FINAL – VERSION-PROOF)

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class NLPEngine:
    def __init__(self):
        # Sentiment
        self.sentiment_model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

        # ✅ Explicit model loading (NO task registry)
        tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
        model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

        self.summarizer = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer
        )

    def summarize_text(self, text, max_length=150, min_length=50):
        output = self.summarizer(
            text,
            max_new_tokens=max_length,
            do_sample=False
        )
        return output[0]["generated_text"]

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
