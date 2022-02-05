#!/bin/bash

socat -dd -T60 TCP-LISTEN:9005,reuseaddr,fork,su=notepad EXEC:/home/notepad/chall,stderr