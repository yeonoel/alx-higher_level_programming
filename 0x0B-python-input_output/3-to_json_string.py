#!/usr/bin/python3
"""To JSON string"""
import json


def to_json_string(my_obj):
    """JSON representation of an object
    Args:
        my_obj(any): the object to represent in JSON
    """
    return (json.dumps(my_obj))
