"""


Given a string `s`, return the length of the longest palindrome that can be
built with those letters.

### Examples

    longest_palindrome("a") ➞ 1
    
    longest_palindrome("bb") ➞ 2
    
    longest_palindrome("abccccdd") ➞ 7
    
    longest_palindrome("") ➞ 0

### Notes

N/A

"""

from collections import Counter as C
def longest_palindrome(s):
  d=dict(C(s))
  lp=0
  for x in d:
    if d[x]%2==0:
      lp+=d[x]
    else:
      lp+=d[x]-1
  lp+=1*any(d[x]%2 for x in d)  
  return lp

