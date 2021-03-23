"""


Create a function that takes a string and returns a new string with its first
and last characters swapped, except under three conditions:

  1. If the length of the string is less than two, return `"Incompatible."`.
  2. If the argument is not a string, return `"Incompatible."`.
  3. If the first and last characters are the same, return `"Two's a pair."`.

### Examples

    flip_end_chars("Cat, dog, and mouse.") ➞ ".at, dog, and mouseC"
    
    flip_end_chars("ada") ➞ "Two's a pair."
    
    flip_end_chars("Ada") ➞ "adA"
    
    flip_end_chars("z") ➞ "Incompatible."
    
    flip_end_chars([1, 2, 3]) ➞ "Incompatible."

### Notes

Tests are case sensitive (e.g. "A" and "a" are not the same character).

"""

def flip_end_chars(txt):
  if len(txt) >= 2 and type(txt) is not list and txt[0] != txt[-1]:
    return txt[-1]+txt[1:-1]+txt[0]
  elif type(txt) is list or txt == "":
    return "Incompatible."
  elif txt[0] == txt[-1]:
    return "Two's a pair."

