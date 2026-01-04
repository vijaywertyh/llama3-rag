import streamlit as st
import requests

st.set_page_config(page_title="LLaMA 3.1 RAG")

st.title("📄 LLaMA 3.1 Document Q&A")

question = st.text_input("Ask a question")

if question:
    response = requests.post(
        "http://localhost:8000/ask",
        json={"question": question}
    ).json()

    st.subheader("Answer")
    st.write(response["answer"])

    st.subheader("Sources")
    st.json(response["sources"])
