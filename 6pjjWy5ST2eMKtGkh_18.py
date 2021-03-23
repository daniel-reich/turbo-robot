"""


Write a function that replaces all letters within a specified range with the
hash symbol `#`.

### Examples

    replace("abcdef", "c-e") ➞ "ab###f"
    
    replace("rattle", "r-z") ➞ "#a##le"
    
    replace("microscopic", "i-i") ➞ "m#croscop#c"
    
    replace("", "a-z") ➞ ""

### Notes

  * The range will always be in order, a.k.a. for `m-n`, character `m` will always come before or equal `n`.
  * Strings will be in lower case letters only.
  * Return an empty string if the input is an empty string.

"""

import string
​
def replace(txt, r):
  low, hi = r.split("-")
  letters = string.ascii_lowercase
  low_i = letters.index(low)
  hi_i = letters.index(hi)
  to_replace = letters[low_i:hi_i+1]
  result = ""
  for letter in txt:
    result += letter if letter not in to_replace else "#"
  return result

