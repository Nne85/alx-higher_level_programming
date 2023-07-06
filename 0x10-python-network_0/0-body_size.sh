
#!/bin/bash
# Get The body  size  from outgoing  request to url introduced as argument
curl -sI "$1" | awk -F':' '/Content-Length/ {print $2}' | cut -d' ' -f2
