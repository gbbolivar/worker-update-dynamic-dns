FROM python:3-alpine3.18

LABEL name="Alpine3 en español Python 3.18" \
    maintainer="elalconxvii@gmail.com"

ARG UID=1000

# Crea usuario para ejecución de comandos
RUN adduser -D -u 1000 usuario \
    && true


RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN pip3 install  --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app
USER usuario
