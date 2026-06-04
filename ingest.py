import os
import warnings
import glob
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.faiss import FAISS

warnings.filterwarnings("ignore")

def ingest_docs():
    rag_dir = "rag"
    if not os.path.exists(rag_dir):
        print(f"Error: {rag_dir} directory not found.")
        return

    pdf_files = glob.glob(os.path.join(rag_dir, "*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in {rag_dir}.")
        return

    all_documents = []
    for pdf_path in pdf_files:
        print(f"Loading {pdf_path}...")
        loader = PyPDFLoader(pdf_path)
        all_documents.extend(loader.load())

    print(f"Splitting {len(all_documents)} pages into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(all_documents)

    print(f"Initializing embeddings model (all-MiniLM-L6-v2) for {len(chunks)} chunks...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("Creating and optimizing vector store (FAISS)...")
    vector_store = FAISS.from_documents(chunks, embeddings)

    print("Saving vector store to 'vectorstore' directory...")
    vector_store.save_local("vectorstore")
    print("Ingestion complete. Multiple documents processed.")

if __name__ == "__main__":
    ingest_docs()
