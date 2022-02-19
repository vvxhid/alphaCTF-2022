FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y socat patchelf && \
    rm -rf /var/lib/apt/lists/*

RUN useradd alpha 
WORKDIR /home/alpha 

COPY ./flag.txt ./ 
COPY ./alpha ./ 
COPY ./libc.so.6 ./ 
COPY ./ld-linux-x86-64.so.2 ./
COPY ./entrypoint.sh ./

RUN patchelf --set-interpreter ./ld-linux-x86-64.so.2 --replace-needed libc.so.6 ./libc.so.6 ./alpha
RUN chmod +x entrypoint.sh chall libc.so.6 ld-linux-x86-64.so.2 && chown -R alpha:alpha .

USER alpha

CMD ["./entrypoint.sh"]

