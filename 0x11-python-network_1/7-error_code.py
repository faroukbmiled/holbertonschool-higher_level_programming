#!/usr/bin/python3
""""takes in a URL, sends a request to the URL"""
from requests import get
from sys import argv

if __name__ == '__main__':
    reqget = get(argv[1])
    if (reqget.status_code >= 400):
        print('Error code: {}'.format(reqget.status_code))
    else:
        print(reqget.text)
