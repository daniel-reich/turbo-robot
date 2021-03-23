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
  words = txt.split(' ')
  cum_len = [0]
  cum_len.append(len(words[0]))
  for word in words [1:]:
    cum_len.append(len(word)+cum_len[-1]+1)
  result = [x for x in cum_len if x <= length]
  return ' '.join(words[:len(result)-1])

