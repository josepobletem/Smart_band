from fastapi import FastAPI
from recommender.workout_engine import WorkoutRecommender

app = FastAPI()
engine = WorkoutRecommender("cardio", height_cm=175, body_fat_pct=15.0)

@app.get("/recommend")
def recommend(hr: int):
    return {"feedback": engine.suggest(hr)}
