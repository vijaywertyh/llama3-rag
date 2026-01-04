from app.llm import load_llm
from app.retriever import retrieve_documents
from app.prompt import RAG_PROMPT

def run_rag(question: str):
    docs = retrieve_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs])

    llm = load_llm()
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    answer = llm(prompt)

    return {
        "answer": answer,
        "sources": [doc.metadata for doc in docs]
    }
