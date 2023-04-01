#!/usr/bin/python3
"""script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8).
"""

import sys
import urllib.error
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
