import os
from src.agent import get_agent
from src.ingestion import ingest_file
from src.vector_store import reset_vector_store
from src.config import DATA_DIR

def setup_data():
    print("Setting up data...")
    reset_vector_store()
    
    sample_text = """
    DocuMind is an AI agent.
    It was created in 2024.
    """
    file_path = DATA_DIR / "agent_test.txt"
    with open(file_path, "w") as f:
        f.write(sample_text)
        
    ingest_file(str(file_path))

def test_agent():
    setup_data()
    
    print("\nInitializing Agent...")
    agent_executor = get_agent()
    
    questions = [
        "What is 100 + 50?",
        "What is DocuMind?",
        "When was DocuMind created?"
    ]
    
    for q in questions:
        print(f"\nQuestion: {q}")
        try:
            response = agent_executor.invoke({"input": q})
            print(f"Final Answer: {response['output']}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_agent()
