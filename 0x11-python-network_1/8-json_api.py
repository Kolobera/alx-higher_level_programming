#!/usr/bin/python3
"""Status with requests"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        payload = {"q": argv[1]}
    else:
        payload = {"q": ""}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        r.json()
        if r.json() == {}:
            print("No result")
        else:
            lp = dict(r.json())
            print(f"[{lp['id']}] {lp['name']}")
    except:
        print("Not a valid JSON")
