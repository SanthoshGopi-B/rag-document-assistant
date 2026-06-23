import streamlit as st

from src.document_loader import load_and_split
from src.vector_store import create_vector_store
from src.rag_pipeline import generate_answer

st.set_page_config(page_title="RAG Document Assistant")

st.title("📄 RAG Document Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    file_path = f"data/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    chunks = load_and_split(file_path)

    vectorstore = create_vector_store(chunks)

    query = st.text_input(
        "Ask a question about the document"
    )

    if query:

        docs = vectorstore.similarity_search(
            query,
            k=3
        )

        answer = generate_answer(
            docs,
            query
        )

        st.subheader("Answer")
        st.write(answer)