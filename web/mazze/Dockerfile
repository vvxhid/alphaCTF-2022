FROM python:3.8-slim-buster

RUN pip3 install flask

WORKDIR /challenge

COPY ./app .

CMD [ "python3","-m","flask","run","--host=0.0.0.0" ]



