#!/usr/bin/python3
"""github challenge"""
import requests
from sys import argv


if __name__ == "__main__":
    re = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    r = requests.get(re)
    commits = r.json()
    i = 0
    for commit in commits:
        if i < 10:
            print("{}: {}".format(commit.get("sha"),
                  commit.get("commit").get("author").get("name")))
            i += 1
