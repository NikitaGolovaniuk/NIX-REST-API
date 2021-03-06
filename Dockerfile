FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
MAINTAINER Nikita Golovaniuk
WORKDIR /NIX-REST-API
ENV FLASK_APP=wsgi.py
COPY requirements.txt .
RUN apt-get update && apt-get -y install sudo
RUN pip install -r requirements.txt
COPY . /NIX-REST-API
EXPOSE 5000
RUN chmod +x ./migrate.sh
CMD ./migrate.sh && gunicorn -b 0.0.0.0:5000 wsgi:app