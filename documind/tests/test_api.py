import requests
import time
import subprocess
import sys
import os

def test_api():
    # Start API in background
    print("Starting API...")
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=os.getcwd(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    try:
        # Wait for startup (model loading takes time)
        time.sleep(30)
        
        # 1. Health Check
        print("\nTesting /health...")
        try:
            response = requests.get("http://127.0.0.1:8000/health")
            print(f"Status: {response.status_code}")
            print(f"Response: {response.json()}")
            assert response.status_code == 200
        except Exception as e:
            print(f"Health check failed: {e}")
            
        # 2. Chat (Math)
        print("\nTesting /chat (Math)...")
        try:
            payload = {"query": "What is 100 + 50?"}
            response = requests.post("http://127.0.0.1:8000/chat", json=payload)
            print(f"Status: {response.status_code}")
            print(f"Response: {response.json()}")
            assert response.status_code == 200
            assert "150" in response.json()["response"]
        except Exception as e:
            print(f"Chat check failed: {e}")

    finally:
        print("\nStopping API...")
        process.terminate()
        process.wait()

if __name__ == "__main__":
    test_api()
