from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from src.config import VECTOR_STORE_DIR, EMBEDDING_MODEL_NAME
import shutil

def get_vector_store():
    """
    Initializes and returns the ChromaDB vector store with HuggingFace embeddings.
    """
    embedding_function = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    
    vector_store = Chroma(
        persist_directory=str(VECTOR_STORE_DIR),
        embedding_function=embedding_function,
        collection_name="documind_collection"
    )
    return vector_store

def reset_vector_store():
    """
    Clears the existing vector store.
    """
    if VECTOR_STORE_DIR.exists():
        shutil.rmtree(VECTOR_STORE_DIR)
    VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
