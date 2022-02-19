#!/bin/sh

EXEC="/home/alpha/alpha"
PORT=9012
socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr