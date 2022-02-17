FROM ubuntu:20.04

RUN apt-get update && upgrade -y 
RUN apt-get install socat patchelf -y 

RUN useradd -m -d /home/bookstore -s /bin/bash -u 1000 bookstore 

WORKDIR /home/bookstore 

COPY ./flag.txt ./
COPY ./chall ./ 
COPY ./libc.so.6 ./ 
COPY ./ld-2.29.so ./ 
COPY ./entrypoint.sh ./ 

RUN patchelf --set-interpreter ./ld-2.29.so --replace-needed libc.so.6 ./libc.so.6 ./chall

RUN chown -R root:bookstore /home/bookstore
RUN chmod 750 /home/bookstore 
RUN chown root:bookstore ./flag.txt 
RUN chmod 440 ./flag.txt 
RUN chmod 550 ./chall 

EXPOSE 9007 

RUN chmod +x ./entrypoint.sh 

CMD ["./entrypoint.sh"]

