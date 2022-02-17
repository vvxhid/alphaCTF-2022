FROM ubuntu:20.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip socat -y 
RUN pip install PyYAML==3.13

RUN useradd -m -d /home/yaml -s /bin/bash -u 1000 yaml 

WORKDIR /home/yaml 

COPY ./flag.txt ./
COPY ./main.py ./
COPY ./entrypoint.sh ./


RUN chown -R root:yaml /home/yaml 
RUN chmod 750 /home/yaml 
RUN chown root:yaml ./flag.txt 
RUN chmod 440 ./flag.txt 
RUN chmod 550 ./main.py 

EXPOSE 8003 

RUN chmod +x ./entrypoint.sh 

CMD ["./entrypoint.sh"]
