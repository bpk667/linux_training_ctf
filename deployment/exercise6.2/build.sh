#!/bin/sh

mkdir app && cd app
echo "flag62{'you_got_the_shell'}" > secret.txt
echo "$(pwgen 12 1)" > .password
gpg --batch --symmetric --passphrase-file .password secret.txt
rm secret.txt
cd ..
tar cvzf app1_compressed_app app/ --remove-files
gzip -n app1_compressed_app
