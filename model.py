import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text

def get_similarity(resume, job_desc):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume, job_desc])
    return cosine_similarity(vectors)[0][1]
