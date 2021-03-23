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
  ret = [s[0]]
  for i in s[1:]:
    if not i == ret[-1]:
      ret.append(i)
  return ''.join(ret)

