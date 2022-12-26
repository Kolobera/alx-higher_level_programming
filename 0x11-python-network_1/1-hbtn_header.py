#!/usr/bin/python3
""" Alx Status """
import urllib.request
import sys


def myStatus():
    """what's my status"""
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print("{}".format(response.getheader("X-Request-Id")))


if __name__ == "__main__":
    myStatus()
