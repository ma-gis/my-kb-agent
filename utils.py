from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)

def load_and_split_pdfs(pdf_paths):
    all_docs = []
    if pdf_paths:
        for pdf_path in pdf_paths:
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
            all_docs.extend(docs)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(all_docs)