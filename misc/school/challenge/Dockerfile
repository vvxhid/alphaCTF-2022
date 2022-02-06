FROM ubuntu:20.04 

RUN apt-get update -y 
RUN apt-get install socat python3 -y 

RUN useradd -m -d /home/school -s /bin/bash -u 1000 school 

WORKDIR /home/school 

ENV PYTHONUNBUFFERED: 1

COPY ./main.py ./ 
COPY ./entrypoint.sh ./

RUN chown -R root:school /home/school 
RUN chmod +x ./main.py 

EXPOSE 8001 

RUN chmod +x ./entrypoint.sh 

CMD ["./entrypoint.sh"]



