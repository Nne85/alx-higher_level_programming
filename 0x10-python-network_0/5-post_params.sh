#!/bin/bash
# Send a POST request with the parameters and display the body of the respons
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
