"""


Write a function that inverts the keys and values of a dictionary.

### Examples

    invert({ "z": "q", "w": "f" })
    ➞ { "q": "z", "f": "w" }
    
    invert({ "a": 1, "b": 2, "c": 3 })
    ➞ { 1: "a", 2: "b", 3: "c" }
    
    invert({ "zebra": "koala", "horse": "camel" })
    ➞ { "koala": "zebra", "camel": "horse" }

### Notes

N/A

"""

def invert(dct):
  d = dict()
  for elem in dct:
    k = dct[elem]
    d[k] = elem
  return d

