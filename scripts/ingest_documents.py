import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.vector_store import save_vector_store

documents = []

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Correct Windows-friendly path
raw_docs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw_docs")

if not os.path.exists(raw_docs_path):
    raise FileNotFoundError(f"{raw_docs_path} does not exist. Create it and add PDF files!")

for file in os.listdir(raw_docs_path):
    if file.lower().endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(raw_docs_path, file))
        pages = loader.load()
        documents.extend(splitter.split_documents(pages))

save_vector_store(documents)
print(" Documents successfully ingested")
