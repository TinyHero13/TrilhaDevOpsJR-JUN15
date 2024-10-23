FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src ./src

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python", "-m", "flask","--app", "src.main", "run"]
