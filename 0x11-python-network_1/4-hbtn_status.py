#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import requests


if "__name__" == __main__:
    resp = request.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
