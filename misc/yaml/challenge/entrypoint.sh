#!/bin/bash

socat -dd -T60 tcp-l:8003,reuseaddr,fork,keepalive,su=yaml exec:"python3 /home/yaml/main.py",stderr