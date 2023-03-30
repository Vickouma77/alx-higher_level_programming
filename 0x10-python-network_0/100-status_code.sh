#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response. no pipe
awk 'NR==1{printf "%s", $2}' test_1 $(curl -sI "$1" -o test_1)
