#!/bin/bash 

socat -dd -T60 TCP-LISTEN:9002,reuseaddr,fork,su=retwin EXEC:/home/pwn/chall,stderr