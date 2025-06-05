from storage.history_logger import log_json
import os
import json

def test_log_json_creates_file():
    """
    Prueba que la función log_json cree el archivo 'session_history.json' y registre correctamente los datos.

    Llama a log_json con un valor de frecuencia cardíaca y un mensaje.
    Verifica que el archivo exista y que el último registro contenga el valor de 'hr' esperado.

    Returns
    -------
    None
    """
    log_json(100, "Mantén ritmo")
    assert os.path.exists("session_history.json")
    with open("session_history.json", "r") as f:
        last_line = f.readlines()[-1]
        record = json.loads(last_line)
        assert record["hr"] == 100