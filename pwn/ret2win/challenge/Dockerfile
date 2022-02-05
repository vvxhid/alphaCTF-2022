FROM ubuntu:20.04 

RUN apt-get update 
RUN apt-get upgrade -y 
RUN apt-get install -y socat 

ARG PASSWORD==retwin 
RUN useradd -m -d /home/pwn -s /bin/bash -u 1000 retwin 
RUN echo "retwin:${PASSWORD}" | chpasswd 

WORKDIR /home/pwn 

COPY ./chall ./
COPY ./flag.txt ./ 
COPY ./entrypoint.sh ./ 

RUN chown root:root ./flag.txt 
RUN chown root:retwin ./chall 

RUN chmod 400 ./flag.txt 
RUN chmod 4410 ./chall 
RUN chmod +x ./entrypoint.sh 

EXPOSE 9002 

CMD ["./entrypoint.sh"]

