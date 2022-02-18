FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y socat patchelf && \
    rm -rf /var/lib/apt/lists/*

RUN useradd secure
WORKDIR /home/secure

COPY ./flag.txt ./
COPY ./chall ./ 
COPY ./libc6_2.27-3ubuntu1.2_amd64.so ./ 
COPY ./ld-2.27.so ./ 
COPY ./entrypoint.sh ./ 

RUN patchelf --set-interpreter ./ld-2.27.so --replace-needed libc.so.6 ./libc6_2.27-3ubuntu1.2_amd64.so ./chall
RUN chmod +x entrypoint.sh chall ld-2.27.so libc6_2.27-3ubuntu1.2_amd64.so && chown -R secure:secure .

USER secure 

CMD ["./entrypoint.sh"]
