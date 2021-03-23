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

def closest_palindrome(n):
  a = n
  b = n
  if str(n) == str(n)[::-1]:
    return n
  while True:
    a += 1
    b -= 1
    if str(a) == str(a)[::-1] and str(b) == str(b)[::-1]:
      return min(a, b)
    if str(a) == str(a)[::-1]:
      return a
    if str(b) == str(b)[::-1]:
      return b

