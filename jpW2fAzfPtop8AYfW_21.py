"""


Write a function that transforms a list of characters into a list of
dictionaries, where:

  1. The keys are the characters themselves.
  2. The values are the ASCII codes of those characters.

### Examples

    to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]
    
    to_dict(["^"]) ➞ [{"^": 94}]
    
    to_dict([]) ➞ []

### Notes

N/A

"""

def to_dict(liste):
    return [{i:ord(i)} for i in liste] if len(liste)>0 else liste

