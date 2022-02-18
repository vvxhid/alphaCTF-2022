#! /bin/sh
echo "Start Run Socat"
socat -dd -T60 tcp-l:9999,reuseaddr,fork,keepalive,su=chall exec:"python chall.py",stderr
