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
  temp1,temp2 = num,num
  while str(temp1) != str(temp1)[::-1]:
    temp1 += 1
  while str(temp2) != str(temp2)[::-1]:
    temp2 -= 1
    
  if abs(num-temp1) != abs(num-temp2):
    return min(temp1,temp2, key = lambda x: abs(num-x))
  else:
    return min(temp1,temp2)

