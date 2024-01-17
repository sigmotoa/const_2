from fastapi import FastAPI

app = FastAPI()

@app.get("/{user}/{year}")
def age(user:str, year:int):
    return{user + " your age is: "+(str)(2024-year)}


@app.get("/")
def home():
    return {"Hello":"sigmotoa says"}

@app.get('/samid')
def home():
    return{
        "nombre":"Samid Amaury Barrera Camargo",
        "Documento":"80808080",
        "Departamento":"Bogota D.C.",
        "Ciudad":"Bogota D.C.",
        "Codigo postal":"101010",
        "Deportes":["Tenis de mesa","Bicicleta de montaña"],
        "Cargo":"Analista de datos",
        "Empresa":"Grupo MOK"

    }

@app.get("/sebastian")
def home():
    return {"hello word" : "wello here"}

@app.get("/sigmotoa")
def sigmotoa():
    return ("Hi, this is sigmotoa")

