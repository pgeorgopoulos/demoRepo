FROM python:2.7.15

LABEL maintainer "Peter Georgopoulos <peter.g.georgopoulos@outlook.com>"

WORKDIR /app

ARG APPENV

ENV APPENV=$APPENV

RUN pip install flask

COPY ./app.py .

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000