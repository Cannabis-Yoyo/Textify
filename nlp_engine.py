import torch
import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from nltk.tokenize import sent_tokenize

nltk.download("punkt")


class NLPEngine:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # ✅ MANUAL SUMMARIZATION MODEL (NO PIPELINE)
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
        self.model.to(self.device)

        # ✅ SENTIMENT PIPELINE (THIS ONE WORKS)
        self.sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def summarize_text(self, text, max_length=150, min_length=50):
        if len(text.split()) < 100:
            return text

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )

        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        summary_ids = self.model.generate(
            inputs["input_ids"],
            max_length=max_length,
            min_length=min_length,
            num_beams=4,
            early_stopping=True
        )

        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    def analyze_sentiment(self, text):
        sentences = sent_tokenize(text)
        results = self.sentiment_analyzer(sentences)

        scores = {"positive": 0, "negative": 0}
        for r in results:
            scores[r["label"].lower()] += r["score"]

        total = sum(scores.values())
        return {
            "overall_sentiment": max(scores, key=scores.get),
            "confidence": round(max(scores.values()) / total, 2)
        }
