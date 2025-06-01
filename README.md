# Local RAG Chatbot (PDFs) with Streamlit, LangChain, ChromaDB, and Ollama

## Requirements

- Python 3.9+
- [Ollama](https://ollama.com/) running locally (for LLM and embedding models)
- (Optional) [virtualenv](https://virtualenv.pypa.io/en/latest/) or similar for Python environments

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/ma-gis/my-kb-agent
   cd my-kb-agent
   ```

2. **Create and activate a virtual environment (recommended):**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Start Ollama and pull required models:**
   - Make sure Ollama is running:  
     ```sh
     ollama serve
     ```
   - Pull the models used in your code (e.g., llama3 and nomic-embed-text):  
     ```sh
     ollama pull llama3
     ollama pull nomic-embed-text
     ```

## Running the App

1. **Start the Streamlit app:**
   ```sh
   streamlit run app_ui.py
   ```

2. **Usage:**
   - Upload one or more PDF files using the UI.
   - Wait for the knowledge base to build.
   - Ask questions about the uploaded PDFs.

## Notes

- Uploaded PDFs are stored in the `.data/` directory (excluded from git).
- The Chroma vector database is stored in the `db/` directory (excluded from git).
- To reset the knowledge base, delete the contents of `.data/` and `db/`.

---