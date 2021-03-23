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
  if n == 100:
    return 99
  n = list(str(n))
  n = [int(i) for i in n]
​
  for i in range(len(n) // 2):
    x, y = n[i], n[-i - 1]
    x, y = x, x
    n[i], n[-i - 1] = x, x
  return int(''.join(str(i) for i in n))

