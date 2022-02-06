#!/bin/bash 


socat -dd -T60 tcp-l:8001,reuseaddr,fork,keepalive,su=school exec:"python3 main.py",stderr