from recommender.workout_engine import WorkoutRecommender

def test_suggestion_ranges():
    """
    Prueba el método suggest de WorkoutRecommender para distintos rangos de frecuencia cardíaca.

    Crea una instancia de WorkoutRecommender con objetivo 'cardio', edad 30, altura 175 cm, 15% de grasa corporal y peso 70 kg.
    Verifica que:
      - Para 90 bpm, la sugerencia contiene 'Aumenta'.
      - Para 120 bpm, la sugerencia contiene 'Mantén'.
      - Para 150 bpm, la sugerencia contiene 'Baja'.
    """
    engine = WorkoutRecommender(
        objective="cardio",
        age=30,
        height_cm=175,
        body_fat_pct=15.0,
        weight_kg=70
    )
    assert "Aumenta" in engine.suggest(90)
    assert "Mantén" in engine.suggest(120)
    assert "Baja" in engine.suggest(150)
