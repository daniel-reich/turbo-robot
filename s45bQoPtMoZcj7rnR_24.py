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

def check_palindrome(num):
  if str(num) == str(num)[::-1]:
    return True
  return False
​
def closest_palindrome(num):
  if check_palindrome(num):
    return num
  else:
    num1 = num ; num2 = num
    while True:
      num1 = num1 - 1
      if check_palindrome(num1):
        diff1 = num - num1
        break
    while True:
      num2 = num2 + 1
      if check_palindrome(num2):
        diff2 = num2 - num
        break
    if diff1 > diff2:
      return num2
    elif diff1 < diff2:
      return num1
    else:
      return num1

