from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class TrendAnalyzer:
    def __init__(self, max_features=20):
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=max_features
        )

    def extract_keywords(self, documents):
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        scores = np.mean(tfidf_matrix.toarray(), axis=0)

        keywords = sorted(
            zip(self.vectorizer.get_feature_names_out(), scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [word for word, score in keywords]
