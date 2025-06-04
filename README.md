# Smartband MVP
# Estructura del proyecto y MVP funcional

# 1. Entorno virtual (Makefile lo maneja)
# 2. Variables adicionales: grasa corporal, estatura, edad, peso
# 3. Feedback según FC
# 4. Comunicación por serial (ESP32 o Arduino)
# 5. Almacenamiento: JSON o SQLite
# 6. API REST con FastAPI (extendida por usuario)
# 7. Docker + docker-compose
# 8. Módulo de gestión de usuarios dinámico
# 9. Interfaz en Python con panel visual
# 10. Pruebas de conexión con Arduino

# Proyecto base: smartband_mvp/

smartband_mvp/
├── api/
│   └── app.py
├── recommender/
│   └── workout_engine.py
├── sensors/
│   ├── heart_rate_simulator.py
│   └── serial_interface.py
├── storage/
│   ├── history_logger.py
│   ├── db_sqlite.py
│   └── user_profile.py
├── gui/
│   └── dashboard.py
├── arduino/
│   └── connection_test.py
├── tests/
│   ├── test_engine.py
│   ├── test_users.py
│   ├── test_arduino.py
│   ├── test_logger.py
│   └── test_api.py
├── session_history.json
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── README.md
└── main.py

## Funcionalidad

- Sugerencias de ejercicios en tiempo real según FC.
- Variables: Estatura, grasa corporal.
- Simulación o conexión real por serial (ESP32).
- API REST con FastAPI.
- Historial en JSON y SQLite.
- GUI con Tkinter.
- Docker y entorno virtual.

## Uso

```bash
make install
make run
```
## Endpoints de la API

### POST /recommend
```json
{
  "heart_rate": 128,
  "height_cm": 175,
  "weight_kg": 70,
  "age": 30,
  "body_fat_pct": 15.2,
  "objective": "cardio"
}
```
**Respuesta:**
```json
{
  "recommendation": "Mantén el ritmo"
}
```

### POST /user/create
```json
{
  "name": "Ana",
  "height_cm": 165,
  "weight_kg": 62,
  "age": 28,
  "body_fat_pct": 18.5,
  "objective": "aerobico"
}
```
**Respuesta:**
```json
{
  "user_id": "UUID generado",
  "name": "Ana",
  "age": 28,
  "height_cm": 165,
  "weight_kg": 62,
  "body_fat_pct": 18.5,
  "objective": "aerobico"
}
```

### Los usuarios se guardan automáticamente en SQLite (`session.db`) en la tabla `users`.

### Interfaz Gráfica
Ejecutar `python gui/dashboard.py` para acceder a una GUI simple.

### Conexión Arduino
Cargar sketch en Arduino que envíe valores de FC por serial. Luego ejecutar:
```bash
python arduino/connection_test.py
```

### Prueba de conexión con Arduino (Mock)
Incluida en `tests/test_arduino.py` usando `monkeypatch` de `pytest`.
