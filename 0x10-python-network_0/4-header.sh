#!/bin/bash
# Send a GET request with the custom header and display response
curl -sH "X-School-User-Id: 98" "$1"
