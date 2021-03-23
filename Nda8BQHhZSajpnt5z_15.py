"""


Write a function that returns the greatest common divisor of all list
elements. If the greatest common divisor is `1`, return `1`.

### Examples

    GCD([10, 20, 40]) ➞ 10
    
    GCD([1, 2, 3, 100]) ➞ 1
    
    GCD([1024, 192, 2048, 512]) ➞ 64

### Notes

  * List elements are always greater than `0`.
  * There is a minimum of two list elements given.

"""

def GCD(lst):
  newdict={}
  for i in range(1, max(lst)):
      for n in lst:
        if n%i==0:
          if i in newdict:
           newdict[i]+=1
          else:
            newdict[i]=1
  newList=[i for i in newdict if newdict[i]==len(lst)]
  return max(newList)

