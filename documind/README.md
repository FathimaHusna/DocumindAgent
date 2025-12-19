# DocuMind: Agentic RAG System

**DocuMind** is an intelligent, agentic Knowledge Retrieval System designed to demonstrate advanced AI/ML engineering capabilities. It combines **RAG (Retrieval-Augmented Generation)** with **Agentic Workflows** to answer questions using both document context and external tools (Calculator).

## Features
-   **Data Ingestion**: Upload PDF/Text files, split them into chunks, and store embeddings in **ChromaDB**.
-   **RAG Pipeline**: Retrieves relevant context using semantic search and generates answers with **Flan-T5**.
-   **Agentic Router**: Dynamically selects between **Search** (for documents) and **Calculator** (for math) tools.
-   **Production API**: Built with **FastAPI** and containerized with **Docker**.

## Tech Stack
-   **Language**: Python 3.11
-   **LLM**: `google/flan-t5-base` (Local, CPU-friendly)
-   **Vector Store**: ChromaDB
-   **Frameworks**: LangChain, FastAPI
-   **Deployment**: Docker

## Setup & Usage

### 1. Local Setup
```bash
# Clone repository
git clone https://github.com/FathimaHusna/DocumindAgent
cd documind

# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn main:app --reload
```

### 2. Docker Setup
```bash
# Build image
docker build -t documind .

# Run container
docker run -p 8000:8000 documind
```

### 3. Vercel Deployment
This project can be deployed to Vercel. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

### 4. API Usage
**Health Check**
```bash
curl http://localhost:8000/health
```

**Ingest Document**
```bash
curl -X POST -F "file=@/path/to/document.pdf" http://localhost:8000/ingest
```

**Chat**
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"query": "What is DocuMind?"}' \
     http://localhost:8000/chat
```
