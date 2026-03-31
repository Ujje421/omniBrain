from fastapi import FastAPI
from brain import run_agent

app = FastAPI(title="OmniBrain GOD LEVEL")

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/ask")
async def ask(query: str):
    return {"response": run_agent(query)}
