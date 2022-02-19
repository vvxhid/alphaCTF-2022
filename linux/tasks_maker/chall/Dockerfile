FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y cron socat
RUN useradd -m -d /ctf -s /bin/bash ctf
RUN echo "ctf:ctf-user-1337" | chpasswd
RUN useradd -r -s /bin/bash ctf-cracked

COPY flag.txt /ctf
COPY chall.sh /ctf
COPY task /etc/cron.d/task
COPY entrypoint.sh /entrypoint.sh

#create tasks list file 
RUN mkdir -m 733 /tmp/tasks

#change files owner

RUN chown ctf-cracked:ctf-cracked /tmp/tasks
RUN chown ctf-cracked:ctf-cracked /ctf/flag.txt
RUN chown ctf-cracked:ctf-cracked /ctf/chall.sh

#change files permissions
RUN chmod 400 /ctf/flag.txt
RUN chmod 544 /ctf/chall.sh
RUN chmod 644 /etc/cron.d/task
RUN chmod +x /entrypoint.sh

# CMD ["su", "-", "ctf", "--command", "socat tcp-listen:1337,fork,reuseaddr EXEC:/bin/bash"]

ENTRYPOINT [ "/entrypoint.sh" ]