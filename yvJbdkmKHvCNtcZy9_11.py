"""


A number is said to be Disarium if the **sum** of its _digits raised to their
respective positions_ is the number itself.

Create a function that determines whether a number is a Disarium or not.

### Examples

    is_disarium(75) ➞ False
    # 7^1 + 5^2 = 7 + 25 = 32
    
    is_disarium(135) ➞ True
    # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
    
    is_disarium(544) ➞ False
    
    is_disarium(518) ➞ True
    
    is_disarium(466) ➞ False
    
    is_disarium(8) ➞ True

### Notes

  * Position of the digit is 1-indexed.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/aifM22oGtRKShsFWB).

"""

def is_disarium(n):
  list1 = []
  a = 1
  total = 0
  for i in str(n):
    list1.append(int(i))
  for i in list1:
    total += i**a
    a+=1
  return total == int(n)

