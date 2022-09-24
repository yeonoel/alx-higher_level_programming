#!/usr/bin/python3
"""This script takes URL, sends a req and of the X-Request-Id"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
