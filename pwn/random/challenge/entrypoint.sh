#!/bin/sh

PORT=9004

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:/home/random/chall,stderr
