#!/bin/bash

adb connect deepnews-app

echo "device is online as user"

# wait until adb is retared as root
sleep 60

echo "Waiting for device to come online as root"
adb connect deepnews-app

echo "adb is connected as root"

su - messenger-user --command "socat tcp-listen:9001,fork,reuseaddr EXEC:'/usr/bin/python3 /app/messenger.py'"