"""


If you take an integer and form the product of its individual digits, you get
a smaller number. Keep doing this and eventually you end up with a single
digit.

The number of steps it takes to reach this point is known as the integer's
_multiplicative persistence_. For example, 347 has a persistence of 3: `3*4*7
= 84, 8*4 = 32, 3*2 = 6`.

Devise a function that returns the persistence of an integer.

### Examples

    persistence(9) ➞ 0
    
    persistence(12) ➞ 1
    
    persistence(6788) ➞ 6
    
    persistence(678852) ➞ 2

### Notes

  * The smallest number with persistence 11 is 277777788888899.
  * A number has never been found, no matter how large, that has a persistence greater than 11.

"""

def persistence(num):
  pcount = 0  # counting the p from 0
  while num >= 10:
    y = num  # temp copy of num
    z = 1  # z holds the value of y as being broken down and multplied
    while (y != 0):
      z = z * (y % 10)  # stripping last number and mult by last z value
      y = y // 10  # integer division, dropping off the last digit
    num = z
    pcount += 1
  return pcount
