from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hello":"sigmotoa says"}


@app.get("/sigmotoa")
def sigmotoa():
    return ("Hi, this is sigmotoa")