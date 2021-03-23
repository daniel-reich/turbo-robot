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
  lst = sorted(lst)
  for i in range(lst[0]):
    if lst[0] % (i+1) == 0:
      temp = lst[0] / (i+1)
      for j in range(len(lst)):
        if lst[j] % temp != 0:
          break
      else: 
        return temp

