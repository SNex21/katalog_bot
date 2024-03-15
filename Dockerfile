FROM python:alpine3.11
WORKDIR /usr/src/cnw

COPY ./req.txt /usr/src/req.txt
RUN pip install --upgrade pip

RUN pip install sqlalchemy aiogram
RUN pip install multidict python-dotenv psycopg2-binary
COPY . usr/src/cnw

EXPOSE 8000
EXPOSE 80