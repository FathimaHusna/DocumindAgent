import os
from src.ingestion import ingest_file
from src.vector_store import get_vector_store, reset_vector_store
from src.config import DATA_DIR

def create_sample_data():
    sample_text = """
    DocuMind is a revolutionary AI system designed to assist with document analysis.
    It uses advanced RAG techniques to retrieve relevant information.
    The system is built using Python, LangChain, and ChromaDB.
    """
    file_path = DATA_DIR / "sample.txt"
    with open(file_path, "w") as f:
        f.write(sample_text)
    return str(file_path)

def test_ingestion():
    # 1. Reset DB
    print("Resetting Vector DB...")
    reset_vector_store()
    
    # 2. Create Sample Data
    print("Creating sample data...")
    file_path = create_sample_data()
    
    # 3. Run Ingestion
    print("Running ingestion...")
    ingest_file(file_path)
    
    # 4. Verify Retrieval
    print("Verifying retrieval...")
    vector_store = get_vector_store()
    results = vector_store.similarity_search("What is DocuMind?", k=1)
    
    if results:
        print(f"Success! Retrieved: {results[0].page_content}")
    else:
        print("Failed to retrieve information.")

if __name__ == "__main__":
    test_ingestion()
