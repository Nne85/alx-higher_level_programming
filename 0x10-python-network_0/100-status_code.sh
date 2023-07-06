#!/bin/bash
#get statue code from http header  work just task(curl -sI "$1" | grep "HTTP/" |  cut -d " " -f 2)
curl -o /dev/null -w '%{http_code}' -sIL "$1"
