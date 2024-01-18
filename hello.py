from fastapi import FastAPI, Query, Path, Body, status
from typing import Optional
from pydantic import BaseModel, Field
from enums import HairColor, Zodiac

class Person(BaseModel):
    first_name:str=Field(
        ...,
        min_lenght=2,
        max_lenght=30,
        example="sigmotoa"
        )
    last_name:str=Field(
        ...,
        min_lenght=2,
        max_lenght=30,
        example="sigmotoa"
        )
    age:int = Field(
        ...,
        gt=0,
        le=140,
        example=54
        )
    hair_color:Optional[HairColor] = Field(
        default=None,
        example=HairColor.BLONDIE
        )
    zodiac:Optional[Zodiac]=Field(
        default=Zodiac.geminis
        )
    married:Optional[bool]=Field(
        default=None,
        example=False
        )


class PersonOut(Person):
    pass

class PersonIn(Person):
    password:str=Field(
        ...,
        min_length=5
        )

class User(BaseModel):
    user_id : int
    user_name : str =Field(...,
                           min_length = 2,
                           max_length = 25)
    user_status : Optional [bool]

app = FastAPI()


@app.post("/person/new", response_model=PersonOut, status_code=status.HTTP_201_CREATED)
def create_person(person:PersonIn=Body(...)):
    return person


@app.put("/user/show/{user_id}")
def show_user(
    user_id:int = Path(...,
                       title="User id :)",
                       gt=0),
    user:User = Body(...)
):
    return user


@app.get("/user/detail/{user_id}")
def user_detail_id(user_id:int =Path(
                    ...,
                    gt=0,
                    title = "User id number",
                    description ="Id for the user")
                    ):
    return {user_id:"ok"}




@app.get("/user/detail")
def user_detail(name:Optional [str] = Query(None, min_length=2, max_length=25),
                age: Optional [int] = Query(...) ):
    return {name:age}



@app.get("/{user}/{year}")
def age(user:str, year:int):
    return{user + " your age is: "+(str)(2024-year)}


@app.get("/", status_code=status.HTTP_200_OK)
def hello():
    return {"Hello":"sigmotoa says"}

@app.get('/samid')
def samid():
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
def sebastiane():
    return {"hello word" : "wello here"}

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
    else: return "escriba bien"
