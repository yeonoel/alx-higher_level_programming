#!/usr/bin/env bash
# takes in a URL, sends a request to that URL, and
# displays the size of the body of the response.
# The size must be displayed in bytes
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2