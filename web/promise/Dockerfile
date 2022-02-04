FROM python:alpine

RUN adduser -D fastapi

WORKDIR /home/fastapi

RUN apk add --update openssl && \
    rm -rf /var/cache/apk/*

RUN openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout key.pem -out cert.pem -subj "/C=US/ST=VA/L=DC/O=OrgName/OU=IT Department/CN=example.com"

RUN pip install fastapi pydantic hypercorn

RUN chown -R fastapi:fastapi ./

COPY app /home/fastapi/app

USER fastapi

EXPOSE 9000

RUN pwd && ls app

CMD ["hypercorn", "--keyfile", "key.pem", "--certfile", "cert.pem", "-b", "0.0.0.0:9000", "app.main:app"]



