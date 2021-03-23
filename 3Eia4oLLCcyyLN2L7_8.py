"""


Create a function that replaces all consecutively repeated letters in a word
with single letters.

### Examples

    remove_repeats("aaabbbccc") ➞ "abc"
    
    remove_repeats("bookkeeper") ➞ "bokeper"
    
    remove_repeats("nananana") ➞ "nananana"

### Notes

N/A

"""

def remove_repeats(s):
  y = []
  for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
      y += [s[x]]
  return "".join(y) + s[-1]

