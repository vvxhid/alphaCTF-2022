#!/bin/bash

crontab /etc/cron.d/task

su - ctf --command "socat tcp-listen:1337,fork,reuseaddr EXEC:/bin/bash"