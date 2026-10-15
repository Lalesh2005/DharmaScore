from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(teacher_answer, student_answer):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([
        teacher_answer,
        student_answer
    ])

    similarity = cosine_similarity(vectors[0], vectors[1])

    score = similarity[0][0] * 100

    return score