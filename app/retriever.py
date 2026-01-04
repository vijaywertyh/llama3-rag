from app.vector_store import load_vector_store
from app.config import TOP_K

def retrieve_documents(query):
    db = load_vector_store()
    return db.similarity_search(query, k=TOP_K)
