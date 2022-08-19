#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        status = response.read()
        print('Body response:')
        print(f'\t- type: {type(status)}')
        print(f'\t- content: {status}')
        print(f"\t- utf8 content: {status.decode('utf-8')}")
