FROM python:3.9-slim-buster

WORKDIR /app
EXPOSE 8000
COPY . .

RUN pip install Flask yfinance
CMD ["python3", "first_run.py"]
CMD ["python3", "app.py"]
