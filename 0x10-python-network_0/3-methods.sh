#!/bin/bash
# curl the thing
curl -sI "$1" | grep Allow: | cut -d " " -f2-
