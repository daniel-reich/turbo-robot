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
  chars = chars.replace('%',' ').replace('&',' ').split(' ')
  total = 0
  for eachnum in chars:
    if '-' in eachnum:
      eachnum = eachnum.split('-')
      total += sum(list([int(x)*-1 for x in eachnum if x != '']))
    else:
      continue
  return total
  #return sum(list([int(x) for x in chars if '-' in x]))

