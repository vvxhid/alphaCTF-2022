#!/bin/bash 

while :; do
    socat -dd -T60 tcp-l:9009,reuseaddr,fork,keepalive,su=alphaecho exec:"python3 main.py",stderr
done