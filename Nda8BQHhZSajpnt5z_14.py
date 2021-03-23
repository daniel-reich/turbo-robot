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

def get_gcd(num1, num2):
  if num2 % num1 == 0:
    return num1
  return get_gcd(num2%num1, num1)
​
​
def GCD(lst):
  size = len(lst)
  if size == 1:
    return lst[0]
  lst.sort()
  comm_div = get_gcd(lst[0], lst[1])
  for value in lst[2:]:
    comm_div = get_gcd(comm_div, value)
  return comm_div

