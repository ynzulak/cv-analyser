from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

from nlp import natural_language_processing

# job_quote = "XYZ is hiring a Python Developer! We're looking for a developer with experience in building scalable applications using Python (Django, Flask, or FastAPI). Work on cloud-based, enterprise-level solutions with a global team. Location: Hybrid (Warsaw or remote in Poland). Full-time, Mid/Senior level. Join us and help shape the future of AI and cloud computing!"

job_quote = "Join XYZ as a Frontend Developer! We're looking for a skilled developer experienced in modern JavaScript frameworks (React, Typescript) to build responsive, user-friendly web applications. Work in a collaborative, innovative environment with global impact. Location: Hybrid (Warsaw or remote in Poland). Full-time, Mid/Senior level. Apply now and shape the future of technology with us!"

def similarity_score(cv_text, data_name):
    model = SentenceTransformer('all-MiniLM-L6-v2') 

    job_text = natural_language_processing(job_quote)
    job_tokens = ' '.join(job_text)

    cv_tokens = ' '.join(cv_text)

    cv_vector = model.encode(cv_tokens)
    job_vector = model.encode(job_tokens)

    similarity = cosine_similarity([cv_vector], [job_vector])[0][0]
    print(f"{data_name}: {similarity:.3f}")  



