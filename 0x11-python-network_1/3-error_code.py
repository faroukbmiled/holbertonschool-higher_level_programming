#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    arg1 = request.Request(argv[1])
    try:
        with request.urlopen(arg1) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as error:
        print('Error code: {}'.format(error.code))
