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
  word = s[0]
  for i in range(1, len(s)):
    if s[i] != s[i-1]:
      word = word + s[i]
  return word

