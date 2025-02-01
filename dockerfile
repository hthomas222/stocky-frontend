FROM python:3.9-slim-buster

WORKDIR /app
EXPOSE 8000
COPY . .

RUN pip install Flask yfinance

CMD ["flask", "run", "--host=0.0.0.0" ":8000"]
