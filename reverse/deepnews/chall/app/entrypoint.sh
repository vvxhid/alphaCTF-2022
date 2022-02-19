#!/bin/bash


# parent image starting point
/bin/sh -c '/usr/bin/supervisord --configuration supervisord.conf' &

# check if emulator is ready
echo "Waiting for Emulator to start"

adb wait-for-device

sleep 10
echo "restarting emulator as root"
# run adb as root
adb root

# wait for device to come online again
adb wait-for-device

while ! adb install /app/app-release.apk > /dev/null 2>&1;
do
  echo -n "."
  sleep 1
done
echo "Emulator started and app is installed"

# copy flag and files to device & fix permissions

adb push /flag.txt /data/data/com.alphactf.deepnews/flag.txt
adb shell chmod +x /data/data/com.alphactf.deepnews
adb shell chown u0_a146:u0_a146 /data/data/com.alphactf.deepnews/flag.txt

while true; 
do 
    sleep 120
    # adb shell am force-stop com.alphactf.deepnews 
done