# syntax=docker/dockerfile:1
FROM python:3.7-slim-buster

COPY ./app /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]