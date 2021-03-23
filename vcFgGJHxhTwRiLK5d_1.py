"""


Given a positive integer `n`, implement a function that finds the **smallest**
number that is evenly divisible by the integers `1` through `n` inclusive.

### Examples

    smallest(1) ➞ 1
    
    smallest(5) ➞ 60
    
    smallest(10) ➞ 2520
    
    smallest(20) ➞ 232792560

### Notes

N/A

"""

def smallest(n):
  x=n
  n=n-1
  while(n>1):
    if(x%n!=0):
      i=1
      while((x*i)%n!=0):
        i+=1
      x=x*i
    n-=1
  return x

