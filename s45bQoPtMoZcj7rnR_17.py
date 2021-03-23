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
  numStr = str(num)
  if numStr == numStr[::-1]:
    return num
  minPalindrome = False
  minNum = num
  maxPalindrome = False
  maxNum = num
  while minPalindrome == False:
    minNum -= 1
    if str(minNum) == str(minNum)[::-1]:
      minPalindrome = True
  while maxPalindrome == False:
    maxNum += 1
    if str(maxNum) == str(maxNum)[::-1]:
      maxPalindrome = True
  if num - minNum < maxNum - num:
    return minNum
  elif num - minNum == maxNum - num:
    return minNum
  else:
    return maxNum

