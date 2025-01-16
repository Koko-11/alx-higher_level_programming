#!/bin/bash
# send a request to an URL with cur
curl -s "$1" | wc -c
