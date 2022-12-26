#!/usr/bin/python3
"""github challenge"""
import requests
from sys import argv


if __name__ == "__main__":
    re = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits"
    r = requests.get(re)
    commits = r.json()
    for commit in commits:
        print("{}: {}".format(commit.get("sha"),
            commit.get("commit").get("author").get("name")))
