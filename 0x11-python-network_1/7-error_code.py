#!/usr/bin/python3
"""Status with requests"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code == requests.codes.ok:
        print("{}".format(r.content.decode("utf-8")))
    else:
        print("Error code:", r.status_code)
