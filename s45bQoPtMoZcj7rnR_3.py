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
  anum = num
  while str(anum) != str(anum)[::-1]:
    anum+=1
  upperlimit=anum
  anum = num
  while str(anum) != str(anum)[::-1]:
    anum-=1
  lowerlimit=anum
  if upperlimit-num < num-lowerlimit:
    return upperlimit
  else:
    return lowerlimit

