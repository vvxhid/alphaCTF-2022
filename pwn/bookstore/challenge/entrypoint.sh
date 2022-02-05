#!/bin/bash

socat -dd -T60 TCP-LISTEN:9007,reuseaddr,fork,su=bookstore EXEC:/home/bookstore/chall,stderr