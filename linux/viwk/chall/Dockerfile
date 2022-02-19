FROM ubuntu:20.04

RUN apt-get update -y 
RUN apt-get upgrade -y
RUN apt install -y socat sudo vim

RUN useradd -m -d /ctf -s /bin/bash ctf

RUN echo "ctf:ctf-vim-jail" | chpasswd

RUN useradd -r -s /bin/bash ctf-cracked
RUN echo "ctf ALL=(ctf-cracked:ctf-cracked) NOPASSWD:/bin/awk" >> /etc/sudoers

WORKDIR /ctf

COPY ./flag.txt .


RUN chown root:ctf-cracked ./flag.txt
RUN chmod 440 ./flag.txt

CMD ["su", "-", "ctf", "--command", "socat tcp-listen:9025,fork,reuseaddr EXEC:/bin/vim"]