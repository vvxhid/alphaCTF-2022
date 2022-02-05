#!/bin/bash

socat -dd -T60 TCP-LISTEN:9004,reuseaddr,fork,su=random EXEC:/home/random/chall,stderr