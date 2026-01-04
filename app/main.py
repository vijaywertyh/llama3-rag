from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse
from app.rag_pipeline import run_rag

app = FastAPI(title="LLaMA 3.1 RAG API")

@app.post("/ask", response_model=QueryResponse)
def ask_question(req: QueryRequest):
    return run_rag(req.question)
