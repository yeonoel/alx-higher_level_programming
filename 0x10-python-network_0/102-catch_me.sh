#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me respond server must contaning  You got me!, in the body of the response.
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool"
