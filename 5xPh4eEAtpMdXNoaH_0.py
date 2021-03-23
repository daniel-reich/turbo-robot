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

from collections import Counter
def longest_palindrome(s):
  cnt = Counter(s)
  odds = sum(v%2 for v in cnt.values())
  return len(s) - max(0, odds-1)

