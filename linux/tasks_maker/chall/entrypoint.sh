#!/bin/bash

crontab /etc/cron.d/task
cron
su - ctf --command "socat tcp-listen:1337,fork,reuseaddr EXEC:/bin/bash"