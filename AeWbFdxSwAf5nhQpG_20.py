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
  cnt=0
  if -10<=num<10:
    return 0
  while len(str(num))>1:
    t=[]
    s=1
    while num>0:
      t.append(num%10)
      num=num//10
    for c in t:
      s=s*c
    num=s
    cnt+=1
  return cnt

