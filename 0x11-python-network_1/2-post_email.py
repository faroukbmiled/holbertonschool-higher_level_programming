#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    arg1 = argv[1]
    email = {'email': argv[2]}
    encoded = parse.urlencode(email).encode()
    post = request.Request(arg1, encoded)
    with request.urlopen(post) as response:
        print(response.read().decode('utf-8'))
