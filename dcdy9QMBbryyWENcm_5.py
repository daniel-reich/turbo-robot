"""


For each of the 6 coffee cups I buy, I get a 7th cup free. In total, I get 7
cups. Create a function that takes `n` cups bought and return the total number
of cups I would get.

### Examples

    total_cups(6) ➞ 7
    
    total_cups(12) ➞ 14
    
    total_cups(213) ➞ 248

### Notes

  * Number of cups I bought + number of cups I got for free.
  * Only valid inputs will be given.

"""

def total_cups(n):
  x = n // 6
  return n + x

