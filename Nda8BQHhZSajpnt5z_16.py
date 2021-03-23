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
  divisors = []
  i=1
  while i<max(lst)/2:
    if max(lst)%i==0:
      divisors.append(i)
    i=i+1
  divisors2 = []
  for y in divisors:
    for x in lst:
      if x%y==0:
        divisors2.append(y)
  current_amount = 0
  for x in divisors:
    new_amount = divisors2.count(x)
    if new_amount >= current_amount:
      current_amount = new_amount
      i = x
  return i

