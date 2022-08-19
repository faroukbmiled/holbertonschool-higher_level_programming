#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from requests import get
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    reqget = get('https://api.github.com/user',
                 auth=HTTPBasicAuth(argv[1], argv[2]))
    id = reqget.json()
    getid = id.get('id')
    print(getid)
