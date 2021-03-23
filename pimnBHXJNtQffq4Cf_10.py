"""


Write a function that creates a dictionary with each **(key, value)** pair
being the **(lower case, upper case)** versions of a letter, respectively.

### Examples

    mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
    
    mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
    
    mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

### Notes

All of the letters in the input list will always be lowercase.

"""

def mapping(letters):
  result = dict()
  for x in letters:
    result[x] = x.upper()
  return result

