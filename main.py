from fastapi import FastAPI
from brain import process_query

app = FastAPI(title="OmniBrain API")

@app.post("/ask")
async def ask(query: str):
    result = process_query(query)
    return {"response": result}
