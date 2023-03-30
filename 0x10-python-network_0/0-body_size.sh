#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response


if [ -z "$1" ]
then
    echo "Please provide a URL as argument"
    exit 1
fi

size=$(curl -s -o /dev/null -w '%{size_download}' "$1")

echo "Response body size: $size bytes"
