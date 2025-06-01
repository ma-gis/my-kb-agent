from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from utils import load_and_split_pdf

def create_vectorstore_from_pdf(pdf_path, persist_directory="db"):
    docs = load_and_split_pdf(pdf_path)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
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
    return chain.run(query)