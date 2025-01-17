#!/usr/bin/python3
""" takes andsends a request to the URL and displays value of variable X-Request-Id """

import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers.get('X-Request-Id')))
