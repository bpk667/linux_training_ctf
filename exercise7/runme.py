import sys
import base64
import random
import string
import lxml
import pytz
import requests
import six
import sqlparse
import codecs
from lorem_text import lorem

usage_msg = "Usage: "+ sys.argv[0] +" (-d/-h)"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To decode the file 'file.txt' (in hexadecimal format), do:\n  $ cat 'file.txt' |python "+ sys.argv[0] +" -d\n"

def isBase64(s):
    try:
        base64.b64encode(base64.b64decode(s)) == s
        print ('Sorry, the base64 module is broken. Decode it before calling the script')
        exit (-1)
    except Exception:
        return False


if len(sys.argv) != 2:
    print(usage_msg)
    sys.exit(1)

if sys.argv[1] == "-d":
    data = input()
    if not isBase64(data):
        try:
            data = bytes.fromhex(data).decode('utf-8')
            for c in data:
                print(lorem.sentence(), file=sys.stderr, end="", flush=False)
                print(c, end="", flush=True)
                print(lorem.sentence(), file=sys.stderr, end="", flush=True)
            print()
            print ("\nOutput can be a mess. Maybe you want to filter the standard error", file=sys.stderr)
        except Exception:
            print('Sorry. Could not decode the string. Is it in hexadecimal format?')
            sys.exit(1)

elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_msg)
    sys.exit(1)

else:
    print("Unrecognized first argument: "+ sys.argv[1])
    print("Please use '-d', or '-h'.")
