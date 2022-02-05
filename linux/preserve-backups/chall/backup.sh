#! /bin/bash

TO_DIR="/opt/backups"

if [[ ! -d $1 ]]; then
    echo "usage: $(basename $0) folder_to_backup " >&2
    exit -1
fi

echo "Backing up files ..."

FOLDER_NAME=$(date +%s)

mkdir "$TO_DIR/$FOLDER_NAME"

cd "$1"

if cp * "$TO_DIR/$FOLDER_NAME" 2> /dev/null ; then
    echo " - Files backed up successfully"
    exit 0
else
    echo " - Some thing went wront :("
    exit -1
fi
