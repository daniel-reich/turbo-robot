"""


Write a function that converts a dictionary into a list, where each element
represents a key-value pair in the form of a list. Sort the list
alphabetically by key.

### Examples

    to_list({ "a": 1, "b": 2 }) ➞ [["a", 1], ["b", 2]]
    
    to_list({ "shrimp": 15, "tots": 12 }) ➞ [["shrimp", 15], ["tots", 12]]
    
    to_list({}) ➞ []

### Notes

Return an empty list if the dictionary is empty.

"""

def to_list(dct):
    return sorted([k, v] for k, v in dct.items())

