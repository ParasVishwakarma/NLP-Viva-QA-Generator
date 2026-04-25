import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def generate_answers(text, questions):
    sentences = nltk.sent_tokenize(text)
    answers = {}

    # Vectorize sentences
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences)

    for q in questions:
        original_q = q  # keep original question for display

        # 🔥 CLEAN QUESTION (IMPORTANT)
        q = q.lower()
        q = q.replace("what is", "").replace("what are", "")
        q = q.replace("explain", "").strip()

        # Convert question to vector
        question_vector = vectorizer.transform([q])

        # Compute similarity
        similarity = cosine_similarity(question_vector, sentence_vectors)

        # Get best matching sentence
        best_match_index = similarity.argmax()

        answers[original_q] = sentences[best_match_index]

    return answers