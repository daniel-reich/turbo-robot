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
  i = 0
  while True:
    a, b = num + i, num - i
    if palindrome(a) or palindrome(b):
      return b if palindrome(b) else a
    i += 1
  
def palindrome(n):
  return str(n) == str(n)[::-1]

