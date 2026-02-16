from nlp_engine import NLPEngine
from trends import extract_keywords
from insights import generate_insights




class Textify:
    def __init__(self):
        self.nlp = NLPEngine()

    def process_text(self, text, max_length=150, min_length=50):
        return {
            "summary": self.nlp.summarize_text(text, max_length, min_length),
            "sentiment": self.nlp.analyze_sentiment(text),
            "keywords": extract_keywords(text),
            "insights": generate_insights(text)
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




