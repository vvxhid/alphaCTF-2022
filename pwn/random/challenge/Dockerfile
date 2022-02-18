FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y socat patchelf && \
    rm -rf /var/lib/apt/lists 

RUN useradd random
WORKDIR /home/random

RUN rm /dev/zero 

COPY ./flag.txt ./ 
COPY ./chall ./ 
COPY ./libc.so.6 ./ 
COPY ./ld-linux-x86-64.so.2 ./ 
COPY ./entrypoint.sh ./ 

RUN patchelf --set-interpreter ./ld-linux-x86-64.so.2 --replace-needed libc.so.6 ./libc.so.6 ./chall

RUN patchelf --set-interpreter ./ld-2.29.so --replace-needed libc.so.6 ./libc.so.6 ./chall
RUN chmod +x entrypoint.sh chall libc.so.6 ld-linux-x86-64.so.2 && chown -R random:random .

USER random

CMD ["./entrypoint.sh"]

