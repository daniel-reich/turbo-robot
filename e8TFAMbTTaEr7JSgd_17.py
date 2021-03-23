"""


Write a function that takes a string as an argument and returns the left most
integer in the string.

### Examples

    left_digit("TrAdE2W1n95!") ➞ 2
    
    left_digit("V3r1ta$") ➞ 3
    
    left_digit("U//DertHe1nflu3nC3") ➞ 1
    
    left_digit("J@v@5cR1PT") ➞ 5

### Notes

  * Each string will have at least two numbers.
  * Return the result as an integer.

"""

import re
​
def left_digit(num):
  x = re.search("\d+", num)
  return int(x.group(0))

