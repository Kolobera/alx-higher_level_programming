#!/usr/bin/python3
"""github challenge"""
import requests
from sys import argv


if __name__ == "__main__":
    re = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits?q=&per_page=100"
    r = requests.get(re)
    commits = r.json()
    i = 0
    for commit in commits:
        if i < 10:
            #if "BEGIN" in str(commit.get("commit").get("verification").get("signature")):
                print("{}: {}".format(commit.get("sha"),
                      commit.get("commit").get("author").get("name")))
                i += 1
