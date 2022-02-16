FROM ubuntu:20.04

WORKDIR /app
RUN apt-get update -y
RUN apt-get install gcc openssl libssl-dev libc-dev musl-dev python3-pip python-dev build-essential -y

RUN openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout key.pem -out cert.pem -subj "/C=US/ST=VA/L=DC/O=OrgName/OU=IT Department/CN=example.com"

RUN pip3 install quart hypercorn aioquic

COPY app /app/

EXPOSE 1337

RUN pwd && ls

ENV FLAG=alphaCTF{4_v3ryyy_qu1cc_tr4nsp0rttt}

CMD ["hypercorn", "--quic-bind", "0.0.0.0:1337" ,"--keyfile", "key.pem", "--certfile", "cert.pem", "-b", "0.0.0.0:80", "main:app"]