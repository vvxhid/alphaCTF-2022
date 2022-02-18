FROM python:3.8-alpine3.12

RUN apk --update add gcc build-base freetype-dev \
    libpng-dev openblas-dev \
    socat tcpdump 

RUN addgroup -S chall && adduser -S chall -G chall

RUN mkdir /chall 
WORKDIR /chall 

COPY ./flag.txt ./
COPY ./chall.py ./ 
COPY ./start.sh ./


RUN chown -R root:chall /chall && \
    chmod 750 /chall && \
    chmod 444 /chall/flag.txt && \
    chmod 550 /chall/chall.py && \
    chmod 550 /chall/start.sh

CMD ["./start.sh"]

EXPOSE 9999