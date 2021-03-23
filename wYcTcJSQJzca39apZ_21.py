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

def truncate(s, ln):
  if ln > len(s):
    return s
  words = s.split()
  if ln < len(s) // 2 and not len(words) % 2:
    return ""
  middle = words[len(words) // 2]
  res = s[:ln]
  res2 = res.split() 
  l = ' '.join([word for word in res2 if word not in middle])
  return l

