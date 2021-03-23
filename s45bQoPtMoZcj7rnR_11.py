"""


Write a function that returns the closest palindrome number to an integer. If
two palindrome numbers tie in absolute distance, return the **smaller
number**.

### Examples

    closest_palindrome(887) ➞ 888
    
    closest_palindrome(100) ➞ 99
    # 99 and 101 are equally distant, so we return the smaller palindrome.
    
    closest_palindrome(888) ➞ 888
    
    closest_palindrome(27) ➞ 22

### Notes

If the number itself is a palindrome, return that number.

"""

def closest_palindrome(num):
  if str(num) == str(num)[::-1]:
    return num
  num_upper = num
  while str(num_upper) != str(num_upper)[::-1]:
    num_upper += 1
  num_lower = num
  while str(num_lower) != str(num_lower)[::-1]:
    num_lower -= 1
  dist_upper = abs(num_upper - num)
  dist_lower = abs(num - num_lower)
  if dist_upper == dist_lower:
    return num_lower
  if dist_upper < dist_lower:
    return num_upper
  if dist_lower < dist_upper:
    return num_lower

