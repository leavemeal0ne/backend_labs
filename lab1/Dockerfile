FROM python:3.11

WORKDIR = /lab1

COPY requirements.txt .

ENV FLASK_APP=lab1.py

ENV PORT=5000

RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE $PORT

CMD flask run --host 0.0.0.0 -p $PORT
