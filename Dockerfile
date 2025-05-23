FROM python:3.13

ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY ./ ./

RUN pip install -r requirements.txt

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app
