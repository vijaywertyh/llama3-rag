from langchain_community.vectorstores import FAISS
from app.embeddings import load_embeddings
from app.config import VECTOR_DB_PATH
import os

def save_vector_store(docs):
    embeddings = load_embeddings()
    db = FAISS.from_documents(docs, embeddings)
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    db.save_local(VECTOR_DB_PATH)

def load_vector_store():
    embeddings = load_embeddings()
    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
