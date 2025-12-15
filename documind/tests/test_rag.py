import os
from src.rag import get_rag_chain
from src.ingestion import ingest_file
from src.vector_store import reset_vector_store
from src.config import DATA_DIR

def setup_data():
    print("Setting up data...")
    reset_vector_store()
    
    sample_text = """
    DocuMind is an advanced AI system for document analysis.
    It supports PDF and Text file ingestion.
    The system uses ChromaDB for vector storage and LangChain for orchestration.
    """
    file_path = DATA_DIR / "rag_test.txt"
    with open(file_path, "w") as f:
        f.write(sample_text)
        
    ingest_file(str(file_path))

def test_rag():
    setup_data()
    
    print("\nInitializing RAG Chain...")
    chain = get_rag_chain()
    
    questions = [
        "What is DocuMind?",
        "What storage does it use?",
        "Does it support PDF?"
    ]
    
    for q in questions:
        print(f"\nQuestion: {q}")
        response = chain.invoke(q)
        print(f"Answer: {response}")

if __name__ == "__main__":
    test_rag()
