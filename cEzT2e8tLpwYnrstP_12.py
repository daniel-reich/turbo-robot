"""


Create a function that takes:

  1. A list of keys.
  2. A list of values (same size).
  3. `True`, if key and value should be swapped, else `False`.

The function returns the constructed dict. Empty lists return an empty dict.

### Examples

    swap_d([1, 2, 3], ["one", "two", "three"], False)
    ➞ { 1: "one", 2: "two", 3: "three" }
    
    swap_d([1, 2, 3], ["one", "two", "three"], True)
    ➞ { "one": 1, "two": 2, "three": 3 }
    
    swap_d(["Paris", 3, 4.5], ["France", "is odd", "is half of 9"], True)
    ➞ { "France": "Paris", "is odd": 3, "is half of 9": 4.5 }

### Notes

  * To make it simple, use only hashable (= immutable) keys.
  * To make it simple, use only unique keys.

"""

def swap_d(k, v, swapped):
  if swapped == True:
    res = {v[i]: k[i] for i in range(len(v))}
  else:
    res = {k[i]: v[i] for i in range(len(k))}
  return res

