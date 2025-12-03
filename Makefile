.PHONY: install test run-cli run-ui run-api help

help:
	@echo "🕵️‍♂️ SpaCy Mood Detective - Makefile Commands"
	@echo ""
	@echo "  make install    - Install dependencies and download spaCy model"
	@echo "  make test       - Run tests"
	@echo "  make run-cli    - Run CLI with example text"
	@echo "  make run-ui     - Start Streamlit web UI"
	@echo "  make run-api    - Start FastAPI server"
	@echo "  make clean      - Clean cache files"

install:
	pip install -r requirements.txt
	python -m spacy download en_core_web_sm

test:
	pytest tests/ -v

run-cli:
	python3 detective.py "I'm too tired to deal with this API today."

run-ui:
	streamlit run app.py

run-api:
	uvicorn api:app --reload --host 0.0.0.0 --port 8000

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

