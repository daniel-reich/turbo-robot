"""


The function is given a string containing digits from `2` to `9`. Return a set
of all possible letter combinations that could represent the digit-string.

### Digits to Letters Mapping

    d = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }

### Examples

    letters_combinations("23") ➞ { "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf" }
    
    letters_combinations("") ➞ set()
    
    letters_combinations("2") ➞ { "a", "b", "c" }

### Notes

N/A

"""

from itertools import product as PD 
def letters_combinations(digits):
  d = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
  A=[d[x] for x in digits]
  if len(digits)>0:
    return {''.join(list(x)) for x in PD(*A)}
  else:
    return set()

