#!/bin/sh

EXEC="./alpha"
PORT=9012
socat -dd -T600 tcp-listen:$PORT,reuseaddr,fork,su=chall EXEC:$EXEC,stderr