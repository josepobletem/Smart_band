# Makefile mejorado
install:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

test:
	. .venv/bin/activate && pytest

lint:
	. .venv/bin/activate && pylint api/ recommender/ storage/ sensors/

ci: install lint test
