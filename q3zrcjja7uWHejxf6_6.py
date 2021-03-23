"""


Create a function that takes a string containing integers as well as other
characters and return the sum of the negative integers only.

### Examples

    negative_sum("-12 13%14&-11") ➞ -23
    # -12 + -11 = -23
    
    negative_sum("22 13%14&-11-22 13 12") ➞ -33
    # -11 + -22 = -33

### Notes

There is at least one negative integer.

"""

def negative_sum(chars):
  def clean(chars):
    for char in chars:
      try:
        i = int(char)
      except ValueError:
        if char != '-':
          chars = chars.replace(char,':')
    
    for n in range(10):
      if '{}-'.format(n) in chars:
        chars = chars.replace('{}-'.format(n), '{}:-'.format(n))
    
    return ''.join([c for c in chars if c != ''])
  
  cleaned = clean(chars)
  ints = [int(i) for i in cleaned.split(':') if i != '']
  
  return sum([i for i in ints if i < 0])

