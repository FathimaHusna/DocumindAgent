import os
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.vector_store import get_vector_store

def load_document(file_path: str) -> List[Document]:
    """
    Loads a document based on its file extension.
    """
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".txt") or file_path.endswith(".md"):
        loader = TextLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
    
    return loader.load()

def split_documents(documents: List[Document]) -> List[Document]:
    """
    Splits documents into smaller chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    return text_splitter.split_documents(documents)

def ingest_file(file_path: str):
    """
    Full ingestion pipeline: Load -> Split -> Store.
    """
    print(f"Loading {file_path}...")
    docs = load_document(file_path)
    
    print(f"Splitting {len(docs)} documents...")
    chunks = split_documents(docs)
    
    print(f"Storing {len(chunks)} chunks in Vector DB...")
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)
    print("Ingestion complete.")
