"""
API para recomendaciones de rutinas de ejercicio y gestión de usuarios.

Este módulo define una API usando FastAPI que permite:
- Recomendar rutinas de ejercicio personalizadas según datos fisiológicos y objetivo del usuario.
- Crear y almacenar perfiles de usuario.

Clases:
--------
UserInput : Modelo de entrada para recomendaciones de ejercicio.
NewUser   : Modelo de entrada para creación de nuevos usuarios.

Endpoints:
----------
POST /recommend
    Recibe datos del usuario y frecuencia cardíaca, devuelve una recomendación de rutina.
POST /user/create
    Recibe datos de un nuevo usuario, lo almacena y retorna el perfil creado.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from recommender.workout_engine import WorkoutRecommender
from storage.user_profile import UserProfile

app = FastAPI()

class UserInput(BaseModel):
    """
    Modelo de entrada para solicitar una recomendación de rutina.

    Atributos
    ---------
    heart_rate : int
        Frecuencia cardíaca actual del usuario.
    height_cm : float
        Altura del usuario en centímetros.
    weight_kg : float
        Peso del usuario en kilogramos.
    age : int
        Edad del usuario en años.
    body_fat_pct : float
        Porcentaje de grasa corporal del usuario.
    objective : str
        Objetivo de entrenamiento del usuario.
    """
    heart_rate: int
    height_cm: float
    weight_kg: float
    age: int
    body_fat_pct: float
    objective: str

class NewUser(BaseModel):
    """
    Modelo de entrada para crear un nuevo perfil de usuario.

    Atributos
    ---------
    name : str
        Nombre del usuario.
    height_cm : float
        Altura del usuario en centímetros.
    weight_kg : float
        Peso del usuario en kilogramos.
    age : int
        Edad del usuario en años.
    body_fat_pct : float
        Porcentaje de grasa corporal del usuario.
    objective : str
        Objetivo de entrenamiento del usuario.
    """
    name: str
    height_cm: float
    weight_kg: float
    age: int
    body_fat_pct: float
    objective: str

@app.post("/recommend")
def recommend(data: UserInput):
    """
    Recomienda una rutina de ejercicio personalizada según los datos del usuario.

    Parámetros
    ----------
    data : UserInput
        Datos fisiológicos y objetivo del usuario.

    Retorna
    -------
    dict
        Recomendación de rutina generada.
    """
    engine = WorkoutRecommender(
        objective=data.objective,
        height_cm=data.height_cm,
        body_fat_pct=data.body_fat_pct,
        weight_kg=data.weight_kg,
        age=data.age
    )
    suggestion = engine.suggest(data.heart_rate)
    return {"recommendation": suggestion}

@app.post("/user/create")
def create_user(data: NewUser):
    """
    Crea y almacena un nuevo perfil de usuario.

    Parámetros
    ----------
    data : NewUser
        Datos del nuevo usuario.

    Retorna
    -------
    dict
        Perfil del usuario creado.
    """
    user = UserProfile(
        name=data.name,
        age=data.age,
        height_cm=data.height_cm,
        weight_kg=data.weight_kg,
        body_fat_pct=data.body_fat_pct,
        objective=data.objective
    )
    user.save_to_db()
    return user.to_dict()