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
  s = str(num)
  m = len(s)//2
  
  if s == s[::-1]:
    return num
  if s.rstrip('0') == '1':
    return num - 1
​
  if len(s)%2:
    return int(s[:m+1] + s[:m][::-1])
  return int(s[:m] + s[:m][::-1])

