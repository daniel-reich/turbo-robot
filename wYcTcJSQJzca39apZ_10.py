"""


Create a function that takes a string (the string to truncate) and a number
(the _maximum_ length of the truncated string) as arguments and returns the
truncated string at the given length.

### Examples

    truncate("Lorem ipsum dolor sit amet.", 11) ➞ "Lorem ipsum"
    
    truncate("Lorem ipsum dolor sit amet.", 16) ➞ "Lorem ipsum"
    
    truncate("Lorem ipsum dolor sit amet.", 17) ➞ "Lorem ipsum dolor"

### Notes

  * To "truncate" means _"to shorten by cutting off the top or end"_.
  * If a word is truncated in the middle, discard it in the output (see 2nd example above).

"""

def truncate(txt, length):
  if length >= len(txt): return txt
  spaces = [k for k, v in enumerate(txt) if v == " "] + [len(txt)]
  if length < spaces[0]: return ""
  for i in range(len(spaces)):
    if spaces[i] > length: return txt[:spaces[i-1]]

