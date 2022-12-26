#!/usr/bin/python3
"""github challenge"""
import requests
from sys import argv


if __name__ == "__main__":
    re = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits"
    r = requests.get(re)
    lp = list(r.json())
    i = 0
    while i < 10:
        lm = dict(lp[i])
        print(f"{lm['sha']}: {lm['commit']['author']['name']}")
        i += 1
