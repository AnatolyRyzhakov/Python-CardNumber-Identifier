FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

COPY . .

# Run Flask app
CMD [".venv/bin/flask", "--app", "app", "run", "--host=0.0.0.0"]