# LLaMA 3.1 RAG Project

**Author:** Vijay Chandhu  
**Date:** 2026-01-03  
**Contact:** [vijaychandhu2000@.com]  

---

## **Project Overview**

This project implements an **end-to-end Retrieval-Augmented Generation (RAG) system** using **LLaMA 3.1**, enabling AI-driven question answering from your own documents. Users can upload PDFs, which are converted into a **FAISS vector database**, and queried via a **FastAPI backend**. The system supports a **Streamlit frontend** for interactive use.  

The goal is to demonstrate how **Gen AI models can be combined with document retrieval** for real-world applications like:

- Company policy assistants  
- Knowledge bases  
- Research document Q&A  
- Product manual support  

---

## **Key Features**

- **Document ingestion**: Load PDFs and automatically split into chunks for embeddings.  
- **Vector storage**: FAISS used for fast similarity search.  
- **Embeddings**: HuggingFace embeddings for semantic understanding.  
- **RAG pipeline**: Combines retrieval with LLaMA 3.1 to generate contextual answers.  
- **FastAPI backend**: Provides endpoints for querying the model programmatically.  
- **Streamlit frontend**: User-friendly web interface for interacting with uploaded documents.  <img width="1163" height="924" alt="Screenshot 2026-01-03 190020" src="https://github.com/user-attachments/assets/e5ffe5a2-ea35-4707-95e7-c37ce64bdc7b" />

- **Windows + Linux compatible**: Full support for local deployment.  
- **Safe FAISS loading**: Secure deserialization options.  

--
