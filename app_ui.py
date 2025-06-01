import streamlit as st
import os
from agent import create_or_load_vectorstore, get_qa_chain, answer_query

st.title("Local RAG Chatbot (PDFs)")

persist_directory = "db"
data_directory = ".data"
os.makedirs(data_directory, exist_ok=True)

uploaded_files = st.file_uploader("Upload one or more PDFs", type="pdf", accept_multiple_files=True)
rebuild_kb = False

if uploaded_files:
    for uploaded_file in uploaded_files:
        pdf_path = os.path.join(data_directory, uploaded_file.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success("PDF(s) uploaded. Building knowledge base...")
    rebuild_kb = True

if rebuild_kb:
    # Build vectorstore from all PDFs in .data/
    pdf_paths = [os.path.join(data_directory, f) for f in os.listdir(data_directory) if f.endswith(".pdf")]
    vectordb = create_or_load_vectorstore(pdf_paths, persist_directory=persist_directory)
    qa_chain = get_qa_chain(vectordb)
    st.session_state["qa_chain"] = qa_chain
    st.success("Knowledge base ready! Ask your questions below.")
elif os.path.exists(persist_directory) and os.listdir(persist_directory):
    if "qa_chain" not in st.session_state:
        vectordb = create_or_load_vectorstore(None, persist_directory=persist_directory)
        qa_chain = get_qa_chain(vectordb)
        st.session_state["qa_chain"] = qa_chain
        st.info("Loaded existing knowledge base. Upload new PDFs to update.")

if "qa_chain" in st.session_state:
    query = st.text_input("Ask a question about the PDFs:")
    if query:
        answer = answer_query(st.session_state["qa_chain"], query)
        st.write("**Answer:**", answer)