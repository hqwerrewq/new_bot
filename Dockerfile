FROM python:3.12

WORKDIR /backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
