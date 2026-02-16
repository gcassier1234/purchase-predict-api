FROM python:3.13-slim

RUN apt update
RUN apt install libgomp1 -y

RUN pip install --upgrade pip
RUN python3 --version

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py
COPY src/ /app/src/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $PORT

CMD exec gunicorn -b :$PORT -w 4 app:app
