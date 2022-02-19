FROM ubuntu:20.04 

RUN apt-get update && apt-get upgrade -y 
RUN apt-get install socat python3 vim -y 

RUN useradd alpha
WORKDIR /home/alphaecho

ENV PYTHONUNBUFFERED: 1

COPY ./flag.txt /home/alphaecho/flag.txt 
COPY ./main.py /home/alphaecho/main.py
COPY ./entrypoint.sh /home/alphaecho/entrypoint.sh 

RUN chmod +x entrypoint.sh main.py && chown -R alpha:alpha . 

EXPOSE 9009

USER alpha
CMD ["./entrypoint.sh"]




