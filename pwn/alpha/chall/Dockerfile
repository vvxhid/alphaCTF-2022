FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -d /home/alpha -s /bin/bash alpha 
WORKDIR /home/alpha 

COPY ./flag.txt ./ 
COPY ./alpha ./ 
COPY ./entrypoint.sh ./

RUN chmod +x entrypoint.sh alpha && chown -R alpha:alpha .

USER alpha

CMD ["./entrypoint.sh"]