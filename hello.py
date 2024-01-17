from fastapi import FastAPI

app = FastAPI()

@app.get("/{user1}/{year}")
def age(user1:str, year:int):
    return{user1 + " your age is: "+(str)(2024-year)}


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
    return {"hello word" : "wello here123"}

@app.get("/sigmotoa")
def sigmotoa():
    return ("Hi, this is sigmotoa")

@app.get("/caballero/{mes}/{dia}")
def zodiaco(mes:str, dia:int):   
    if mes == "febrero" and dia <= 18 or mes == "enero" and dia >= 20:
        return {"camus de acuario"}
    elif mes == "marzo" and dia <= 20 or mes == "febrero" and dia >= 19:
        return {"afrodita de piscis"}
    elif mes == "abril" and dia <= 19 or mes == "marzo" and dia >= 21:
        return {"mu de aries"}
    elif mes == "mayo" and dia <= 20 or mes == "abril" and dia >= 20:
        return {"aldebaran de tauro"}
    elif mes == "junio" and dia <= 20 or mes == "mayo" and dia >= 21:
        return {"saga geminis"}
    elif mes == "julio" and dia <= 22 or mes == "junio" and dia >= 21:
        return {"deathmask cancer"}
    elif mes == "agosto" and dia <= 22 or mes == "julio" and dia >= 23:
        return {"aioria de leo"}
    elif mes == "septiembre" and dia <= 22 or mes == "agosto" and dia >= 23:
        return {"shaka de virgo"}
    elif mes == "octubre" and dia <= 22 or mes == "septiembre" and dia >= 23:
        return {"dohko de libra"}
    elif mes == "noviembre" and dia <= 21 or mes == "octubre" and dia >= 23:
        return {"milo de esccorpio"}
    elif mes == "diciembre" and dia <= 21 or mes == "noviembre" and dia >= 22:
        return {"aioros de sagitario"}
    elif mes == "enero" and dia <= 19 or mes == "siciembre" and dia >= 22:
        return {"shura de caricornio"}
    else: return {"escriba bien"}

@app.get("/nprimos/{var}")
def calprimos(var:int):
    return {(str)(var)}
