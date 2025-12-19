from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import shutil
import os
from src.ingestion import ingest_file
from src.agent import get_agent
from src.config import DATA_DIR

from contextlib import asynccontextmanager

agent = None



app = FastAPI(title="DocuMind API", description="Agentic RAG System")

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    try:
        file_path = DATA_DIR / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        ingest_file(str(file_path))
        return {"message": f"Successfully ingested {file.filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    global agent
    if not agent:
        print("Loading agent for the first time...")
        agent = get_agent()
        print("Agent loaded.")
        
    try:
        if not agent:
            raise HTTPException(status_code=503, detail="Agent not initialized")
        result = agent.invoke({"input": request.query})
        return {"response": result["output"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
