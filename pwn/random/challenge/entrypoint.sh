#!/bin/sh

EXEC="./chall"
PORT=9004

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr
