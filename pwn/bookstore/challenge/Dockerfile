FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y socat patchelf && \
    rm -rf /var/lib/apt/lists/*

RUN useradd bookstore 
WORKDIR /home/bookstore 

COPY ./flag.txt ./ 
COPY ./chall ./ 
COPY ./libc.so.6 ./ 
COPY ./ld-2.29.so ./
COPY ./entrypoint.sh ./

RUN patchelf --set-interpreter ./ld-2.29.so --replace-needed libc.so.6 ./libc.so.6 ./chall
RUN chmod +x entrypoint.sh chall libc.so.6 ld-2.29.so && chown -R bookstore:bookstore .

USER bookstore 

CMD ["./entrypoint.sh"]
