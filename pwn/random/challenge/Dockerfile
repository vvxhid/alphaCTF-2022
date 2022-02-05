FROM ubuntu:20.04 

RUN apt-get update -y 
RUN apt-get install socat patchelf -y 

RUN useradd -m -d /home/random -s /bin/bash -u 1000 random 

RUN rm /dev/zero 

WORKDIR /home/random 

COPY ./flag.txt ./ 
COPY ./chall ./ 
COPY ./libc.so.6 ./ 
COPY ./ld-linux-x86-64.so.2 ./ 
COPY ./entrypoint.sh ./ 

RUN patchelf --set-interpreter ./ld-linux-x86-64.so.2 --replace-needed libc.so.6 ./libc.so.6 ./chall

RUN chown -R root:random /home/random 
RUN chmod 750 /home/random 
RUN chown root:random ./flag.txt 
RUN chmod 440 ./flag.txt 
RUN chmod 550 /home/random/chall 

EXPOSE 9004 

RUN chmod +x ./entrypoint.sh 

CMD ["./entrypoint.sh"]

