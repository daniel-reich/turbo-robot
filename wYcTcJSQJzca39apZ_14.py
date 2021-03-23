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
  wds = txt.split()
  n = 0
  res = ''
  for w in wds:
    n += len(w) + 1
    if n <= length+1:
      res = res + w + ' '
  return res[:-1]

