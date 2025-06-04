class WorkoutRecommender:
    def __init__(self, objective: str, height_cm: float, body_fat_pct: float):
        self.objective = objective
        self.height_cm = height_cm
        self.body_fat_pct = body_fat_pct
        self.zones = {
            "cardio": (110, 140),
            "potencia": (80, 110),
            "aerobico": (120, 160),
        }

    def suggest(self, heart_rate: int) -> str:
        low, high = self.zones.get(self.objective, (100, 140))
        if heart_rate < low:
            return "Aumenta intensidad"
        elif heart_rate > high:
            return "Baja intensidad"
        return "Mantén el ritmo"
