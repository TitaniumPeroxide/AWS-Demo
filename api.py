from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    value: float

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.post("/predict/")
def predict(item: Item):
    result = item.value * 2  # Dummy prediction logic
    return {"name": item.name, "result": result}
