from storage.history_logger import log_json
import os
import json

def test_log_json_creates_file():
    log_json(100, "Mantén ritmo")
    assert os.path.exists("session_history.json")
    with open("session_history.json", "r") as f:
        last_line = f.readlines()[-1]
        record = json.loads(last_line)
        assert record["hr"] == 100