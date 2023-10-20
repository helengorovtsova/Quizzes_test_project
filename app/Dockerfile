FROM python:3.9.18-slim-bullseye

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8080

CMD ["sh", "-c", "python3 main.py && uvicorn main:app --host 0.0.0.0 --port 80"]
