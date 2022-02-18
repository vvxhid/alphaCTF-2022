FROM ubuntu:20.04 

RUN apt update && apt install adb socat python3 -y

ARG messenger_PASSWORD=messenger-password
RUN useradd -m -d /home/messenger-user -s /bin/bash -u 1000 messenger-user

COPY messenger.py /app/messenger.py
RUN chmod +x /app/messenger.py

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
