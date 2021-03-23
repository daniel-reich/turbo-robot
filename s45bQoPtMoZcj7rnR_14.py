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
  a = 0
  b = 0
  c = 1
  while str(num)!=str(num)[::-1]:
    a = str(num-c)
    if a==a[::-1]:
      return int(a)
    b = str(num+c)
    if b==b[::-1]:
      return int(b)
    c+=1
  return num

