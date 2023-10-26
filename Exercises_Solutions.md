# CTF exercises

## 1. Test terminal: `wget` and Internet/lab access (pg. 55)

Entry point: https://linuxctf.ddns.net/ 

Solution:
```
wget http://linuxctf.ddns.net/ 
```

## 2. Base64 and pipes. (pg. 68)

Entry point: https://drive.proton.me/urls/T034ZTH94R#oVZmVcn177gD

Solution:
```
cat not_so_secret |base64 -d |python hex2str.py -d  2>/dev/null 
```

Paranoid/one-liner solution:
```
base64 -d not_so_secret  | xxd -r -p
```

## 3. Iterate with `wget` or `curl`. (pg. 79)

Entry point: https://linuxctf.ddns.net/shop.html

Solution:
```
for i in {4..72} ; do echo $i && wget --wait=0.5 -q https://linuxctf.ddns.net/${i}/ -O- ; done |grep flag
```

Paranoid/one-liner solution (careful with the rate limits):
```
wget --wait=0.5 -q https://linuxctf.ddns.net/{4..70}/ -O- |grep flag
curl --rate 2/s -i https://linuxctf.ddns.net/{4..71}/ 2>&1 |grep flag
```

## 4. runme (pg. 91)

Entry point: https://drive.proton.me/urls/S5Y8ZD0ZMC#mnu0o3VLiXyR

Solution:
```
chmod +x runme && ./runme
```

Paranoid/one-liner solution:
```
strings runme | grep flag
```

## 5. Recursive download (pg. 102)
Entry point: https://linuxctf.ddns.net/recursive/

Solution:
```
wget -r linuxctf.ddns.net/recursive/
grep -ri flagx linuxctf.ddns.net
```

## 6. Command tar and process result (pg. 108)

### 6.1. Commands tar and find.

Entry point: https://drive.proton.me/urls/KJW0CY6XG8#HeHKCBETLQAM

Solution:
```
tar xzf etc_bck.tgz
find etc_bck/ -type f -exec cat {} +
```

Paranoid/one-liner solution:
```
tar -Oxzf etc_bck.tgz etc_bck/cron.daily/creds/password.txt
```

### 6.2. Commands tar & GPG (plus install GPG if necessary)

Entry point: https://drive.proton.me/urls/88EC74QF2W#xpqN3vYIWgta

Solution:
```
gunzip app1_compressed_app.gz
file app1_compressed_app
tar xzf app1_compressed_app
gpg -d  --batch --passphrase-file app/.password app/secret.txt.gpg
```

Paranoid/one-liner solution:
```
gunzip app1_compressed_app.gz; tar -Oxzf app1_compressed_app app/.password | gpg --batch --passphrase-fd 0 -d <(tar -Oxzf app1_compressed_app app/secret.txt.gpg)
```

## 7. Install python dependencies (pg. 148)

Entry point: https://drive.proton.me/urls/9VNBR2A0G0#R8j8UuIiXhTY

Solution:
```
python -m venv  ~/.venvs/training
source ~/.venvs/training/bin/activate
python -m ensurepip --upgrade
pip install -r requirements.txt
cat another_secret |python ./runme.py -d 2>/dev/null
```

Paranoid/one-liner solution:
```
xxd -r -p another_secret
```

## 8. Docker flags (pg. 164)

There are 3 flags (`docker_flag`) in the following image.

Entry point:
```
docker pull pedropozuelo/linuxctf
```

First flag. Solution:
```
docker inspect pedropozuelo/linuxctf |grep flag
```

Second flag. Solution:
```
docker run pedropozuelo/linuxctf cat run.sh
```

Third flag. Solution:
```
mkdir image && cd image
docker save pedropozuelo/linuxctf -o image.tgz
tar xf image.tgz
find . -type f -name "*tar" |while read file ; do tar -Oxf $file ; done |grep -a docker_flag
```

