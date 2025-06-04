import json
from datetime import datetime

def log_json(hr, feedback):
    with open("session_history.json", "a") as f:
        f.write(json.dumps({"timestamp": datetime.now().isoformat(), "hr": hr, "feedback": feedback}) + "\n")
