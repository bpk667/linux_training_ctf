#!/bin/sh

mkdir etc_bck && cd etc_bck
rsync -av -f"+ */" -f"- *" /etc/ ./
mkdir cron.daily/creds
echo "flag61{'you_found_the_needle'}" > cron.daily/creds/password.txt
cd ..
tar czf etc_bck.tgz etc_bck --remove-files
