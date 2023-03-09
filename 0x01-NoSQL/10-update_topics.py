#!/usr/bin/env python3
"""Task 10 module """


def update_topics(mongo_collection, name, topics):
    """
    A  Python function that changes all topics of a school document based on the name
    """
    query = { "name": name }
    new_value = { "$set": { "topics": topics } }
    return mongo_collection.update_many(query, new_value)