"""


Create a function that takes three arguments (first dictionary, second
dictionary, key) in order to:

  1. Return the boolean `True` if both dictionaries have the same values for the same keys.
  2. If the dictionaries don't match, return the string `"Not the same"`, or the string `"One's empty"` if only one of the dictionaries contains the given key.

### Examples

    dict_first = { "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" }
    dict_second = { "people": 12, "sun": "star", "book": "bad" }
    
    check(dict_first, dict_second, "horde") ➞ "One's empty"
    
    check(dict_first, dict_second, "people") ➞ True
    
    check(dict_first, dict_second, "sun") ➞ "Not the same"

### Notes

  * Dictionaries are an unordered data type.
  * Double quotes may be helpful.
  * `KeyError` can occur when trying to access a dictionary key that doesn't exist.

"""

def check(d1, d2, k):
    try:
        return d1[k]==d2[k] or "Not the same"
    except KeyError:
        return "One's empty"

