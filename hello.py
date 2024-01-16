from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hello":"sigmotoa says"}

@app.get("/sebastian")
def home():
    return {"hello word" : "wello here"}

