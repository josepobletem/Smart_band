from sensors.serial_interface import read_serial_data
from recommender.workout_engine import WorkoutRecommender
from storage.db_sqlite import init_db, log_sqlite

init_db()
engine = WorkoutRecommender("cardio", 175, 14.0)

for _ in range(10):
    hr = read_serial_data()
    if hr:
        suggestion = engine.suggest(hr)
        log_sqlite(hr, suggestion)
        print(f"[HR: {hr}] -> {suggestion}")
