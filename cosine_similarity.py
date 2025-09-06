from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

from nlp import natural_language_processing

def similarity_score(job_quote, cv_text, data_name):
    model = SentenceTransformer('all-MiniLM-L6-v2') 

    job_text = natural_language_processing(job_quote)
    job_tokens = ' '.join(job_text)

    cv_tokens = ' '.join(cv_text)

    cv_vector = model.encode(cv_tokens)
    job_vector = model.encode(job_tokens)

    similarity = cosine_similarity([cv_vector], [job_vector])[0][0]
    print(f"{data_name}: {similarity:.3f}")  



