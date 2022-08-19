#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user"""
from requests import post
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    reqpost = post("http://0.0.0.0:5000/search_user", {'q': q})
    try:
        if reqpost.json():
            print('[{}] {}'.format(reqpost.json().get('id'),
                                   reqpost.json().get('name')))
        else:
            print('No result')
    except ValueError as error:
        print('Not a valid JSON')
