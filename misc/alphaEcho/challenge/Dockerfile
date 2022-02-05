FROM ubuntu:20.04 

RUN apt-get update -y 
RUN apt-get install socat python3 vim -y 

RUN useradd -m -d /home/alphaecho -s /bin/bash -u 1000 alphaecho 

WORKDIR /home/alphaecho

ENV PYTHONUNBUFFERED: 1

COPY ./flag.txt /home/alphaecho/flag.txt 
COPY ./main.py /home/alphaecho/main.py
COPY ./entrypoint.sh /home/alphaecho/entrypoint.sh 

RUN chown -R root:alphaecho /home/alphaecho
RUN chmod 750 /home/alphaecho
RUN chmod +x ./main.py 

EXPOSE 9009

RUN chmod +x ./entrypoint.sh 

CMD ["./entrypoint.sh"]




