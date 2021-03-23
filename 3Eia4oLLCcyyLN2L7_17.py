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
  lst = []
  for i in range(len(s)-1):
    if s[i+1] != s[i]: lst.append(s[i])
  if s[-1] != lst[-1]: lst.append(s[-1])
  return "".join(lst)

