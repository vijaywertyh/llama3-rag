from langchain_community.llms import Ollama
from app.config import LLM_MODEL

def load_llm():
    return Ollama(
        model=LLM_MODEL,
        temperature=0.2
    )
