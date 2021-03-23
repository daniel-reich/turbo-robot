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
  def is_pal(num):
    chrs = list(str(num))
    if chrs == chrs[::-1]:
      return True
    return False
  i = num
  j = num
  if is_pal(num):
    return num
  while i>0:
    i -= 1
    j += 1
    if is_pal(i):
      return i
    if is_pal(j):
      return j

