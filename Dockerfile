FROM python:3.9
MAINTAINER Nikita Golovaniuk
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
WORKDIR NIX-REST-API
ENV FLASK_APP=wsgi
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install psycopg2-binary
COPY . .
COPY migrate.sh .
CMD exec ./migrate.sh
EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app