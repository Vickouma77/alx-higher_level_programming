#!/usr/bin/python3
"""Python script that fetches
https://alx-intranet.hbtn.io/status
"""


if __name__ == __main__:
    
    import urllib

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as hbtn:
        content = hbtn.read()
