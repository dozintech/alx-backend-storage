#!/usr/bin/env python3
"""Task 9 module"""


def insert_school(mongo_collection, **kwargs):
    """
    A Python function that inserts a new document in a collection
    based on kwargs
    """
    docs = mongo_collection.insert_one(kwargs)
    return docs.inserted_id
