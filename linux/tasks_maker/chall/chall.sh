#!/bin/bash

#easy bash script 

dir = "/tmp/tasks/"

cd $dir && ls -1a | while read task ; do 
    if [ -x "$dir$task" ] ; then 
        bash -p "$dir$task" 
        rm -f "$dir$task" 
    fi 
done
