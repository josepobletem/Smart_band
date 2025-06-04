from recommender.workout_engine import WorkoutRecommender

def test_suggestion_ranges():
    engine = WorkoutRecommender("cardio", 175, 15.0)
    assert "Aumenta" in engine.suggest(90)
    assert "Mantén" in engine.suggest(120)
    assert "Baja" in engine.suggest(150)
