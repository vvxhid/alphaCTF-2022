FROM ubuntu:20.04  

RUN apt-get update -y 
RUN apt-get install socat patchelf -y 

RUN useradd -m -d /home/notepad -s /bin/bash -u 1000 notepad

WORKDIR /home/notepad 

COPY ./flag.txt ./
COPY ./chall ./ 
COPY ./libc6_2.27-3ubuntu1.2_amd64.so ./ 
COPY ./ld-2.27.so ./ 
COPY ./entrypoint.sh ./ 

RUN patchelf --set-interpreter ./ld-2.27.so --replace-needed libc.so.6 ./libc6_2.27-3ubuntu1.2_amd64.so ./chall

RUN chown -R root:notepad /home/notepad 
RUN chmod 750 /home/notepad 
RUN chown root:notepad ./flag.txt 
RUN chmod 440 ./flag.txt 
RUN chmod 550 ./chall 

EXPOSE 9005 

RUN chmod +x ./entrypoint.sh 

CMD ["./entrypoint.sh"]
