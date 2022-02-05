FROM ubuntu:20.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat sudo

ARG BACKUP_PASSWORD=backup-password

RUN useradd -m -d /home/backup-user -s /bin/bash -u 1000 backup-user
RUN echo "backup-user:${BACKUP_PASSWORD}" | chpasswd

RUN useradd -r -s /bin/bash -u 1001 backup-cracked-user

WORKDIR /home/backup-user

COPY backup.sh .
COPY flag.txt .

RUN echo "backup-user ALL=(backup-cracked-user:backup-cracked-user) NOPASSWD:/home/backup-user/backup.sh" >> /etc/sudoers

RUN mkdir /opt/backups

# change owners
RUN chown -R backup-cracked-user:backup-cracked-user /opt/backups
RUN chown backup-cracked-user:backup-cracked-user flag.txt
RUN chown backup-cracked-user:backup-cracked-user backup.sh

# change permessions
RUN chmod 400 flag.txt
RUN chmod 555 backup.sh
RUN chmod 771 /opt/backups


CMD ["su", "-", "backup-user", "--command", "socat tcp-listen:9001,fork,reuseaddr EXEC:/bin/bash"]
