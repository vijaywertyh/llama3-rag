
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import EMBEDDING_MODEL

def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
