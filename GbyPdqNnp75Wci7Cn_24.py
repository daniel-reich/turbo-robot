"""


Count the amount of ones in the _binary representation_ of an integer. For
example, since 12 is _1100_ in binary, the return value should be `2`.

### Examples

    count_ones(0) ➞ 0
    
    count_ones(100) ➞ 3
    
    count_ones(999) ➞ 8

### Notes

The input will always be a valid integer (number).

"""

def count_ones(num):
  string = bin(num)
  count = 0
  for x in range(0,len(string)):
    if string[x] == '1' : count+=1
  return count

