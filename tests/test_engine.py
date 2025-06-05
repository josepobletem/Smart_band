from recommender.workout_engine import WorkoutRecommender

def test_suggestion_ranges():
    """
    Prueba el método suggest de WorkoutRecommender para distintos rangos de frecuencia cardíaca.

    Crea una instancia de WorkoutRecommender con objetivo 'cardio', altura 175 cm y 15% de grasa corporal.
    Verifica que:
      - Para 90 bpm, la sugerencia contiene 'Aumenta'.
      - Para 120 bpm, la sugerencia contiene 'Mantén'.
      - Para 150 bpm, la sugerencia contiene 'Baja'.

    Returns
    -------
    None
    """
    engine = WorkoutRecommender("cardio", 175, 15.0)
    assert "Aumenta" in engine.suggest(90)
    assert "Mantén" in engine.suggest(120)
    assert "Baja" in engine.suggest(150)
