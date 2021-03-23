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

from collections import Counter as cnt
def longest_palindrome(s):
  cs,odd,res = cnt(s),False,0
  for v in cs.values():
    if v&1:
      odd = True
      res += v-1
    else:
      res += v
  return res + odd

