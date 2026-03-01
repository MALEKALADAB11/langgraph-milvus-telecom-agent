from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Telecom Agent")

class CustomerRequest(BaseModel):
    name: str
    category: str
    budget: float

@app.get("/api/products")
async def get_products():
    return {"status": "success"}

@app.post("/api/recommend")
async def recommend(request: CustomerRequest):
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)