#!/bin/bash
# This script takes a URL, sends a POST
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
