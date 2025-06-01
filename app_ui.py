import streamlit as st
import os
from agent import create_vectorstore_from_pdf, get_qa_chain, answer_query

st.title("Local RAG Chatbot (PDF)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    pdf_path = os.path.join(".data", uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("PDF uploaded. Building knowledge base...")
    vectordb = create_vectorstore_from_pdf(pdf_path)
    qa_chain = get_qa_chain(vectordb)
    st.session_state["qa_chain"] = qa_chain
    st.success("Knowledge base ready! Ask your questions below.")

if "qa_chain" in st.session_state:
    query = st.text_input("Ask a question about the PDF:")
    if query:
        answer = answer_query(st.session_state["qa_chain"], query)
        st.write("**Answer:**", answer)