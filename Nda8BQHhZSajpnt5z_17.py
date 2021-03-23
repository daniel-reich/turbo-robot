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
  li=[]
  for i in lst:
    lis=[]
    for j in range(1,i+1):
      if i%j==0:
        lis.append(j)
      else:
        continue
    li.append(lis)
  sets=[set(x) for x in li[1:]]
  return max(list(set(li[0]).intersection(*sets)))

