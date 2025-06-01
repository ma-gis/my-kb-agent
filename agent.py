import os
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from utils import load_and_split_pdf

def create_or_load_vectorstore(pdf_paths, persist_directory="db"):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    # Check if DB exists and is non-empty
    if os.path.exists(persist_directory) and os.listdir(persist_directory):
        vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    else:
        # pdf_paths can be None or a list
        from utils import load_and_split_pdfs
        docs = load_and_split_pdfs(pdf_paths)
        vectordb = Chroma.from_documents(
            documents=docs,
            embedding=embeddings,
            persist_directory=persist_directory
        )
        vectordb.persist()
    return vectordb

def get_qa_chain(vectorstore):
    llm = Ollama(model="llama3.1:8b")
    retriever = vectorstore.as_retriever()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

def answer_query(chain, query):
    try:
        return chain.run(query)
    except Exception as e:
        return f"Error: {e}"