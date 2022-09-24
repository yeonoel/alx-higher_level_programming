#!/usr/bin/python3
"""This script takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with
    the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    sa = sys.argv[1]
    if len(sa) > 1:
        q = sa
    else:
        q = ""

    resp = requests.post(sys.argv[1], data={'q': q})
    try:
        dic = resp.json()
        if dic == {}:
            print('No result')
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
    except ValueError:
        print('Not a valid JSON')
