#!/usr/bin/python3
""" Alx Status """
import urllib.request
import sys
from urllib.error import HTTPError


def myStatus():
    """what's my status"""
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    myStatus()
