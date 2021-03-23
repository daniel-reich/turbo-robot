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
  s = list(s)
  i = 1
  while i < len(s):
    while i < len(s) and s[i] == s[i-1]:
      s.pop(i)
    i += 1
  return ''.join(s)

