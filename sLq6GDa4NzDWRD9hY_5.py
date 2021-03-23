"""


Create a function that _counts_ the integer's **number of digits**.

### Examples

    count(318) ➞ 3
    
    count(-92563) ➞ 5
    
    count(4666) ➞ 4
    
    count(-314890) ➞ 6
    
    count(654321) ➞ 6
    
    count(638476) ➞ 6

### Notes

  * Solve this **without using strings**.
  * Alternatively, you can solve this via a _recursive approach_.
  * A _recursive_ version of this challenge can be found via this [link](https://edabit.com/challenge/ntJXZh4W8khX9nLPG).

"""

def count(n):
  l = 1
  if n <= 0:
    n = -n
    for i in (10,100,1000,10000,100000,1000000,10000000,100000000):
      if n / i >= 1:
        l += 1
    return l
  else:
    for i in (10,100,1000,10000,100000,1000000,10000000,100000000):
      if n / i >= 1:
        l += 1
    return l

