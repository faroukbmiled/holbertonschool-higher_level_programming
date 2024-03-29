#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
from requests import post
from sys import argv

if __name__ == "__main__":
    print(post(argv[1], {'email': argv[2]}).text)
