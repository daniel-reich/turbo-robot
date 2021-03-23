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

# Functions 
def additive_persistence(n):
 n_str=str(n)
 count=0
 # while length of n_str > 1
 # print("length ",len(n_str))
 while len(n_str) > 1:
  add=0
  # go through string elements
  for i in range(0,len(n_str)):
   # turn to int
   # add to sum
   add+=int(n_str[i])
  count+=1
  n_str=str(add)
 return count
​
def persistence(n):
 n_str=str(n)
 count=0
 while len(n_str) > 1:
  prod=1
  for i in range(0,len(n_str)):
   prod*=int(n_str[i])
  count+=1
  n_str=str(prod)
 return count

