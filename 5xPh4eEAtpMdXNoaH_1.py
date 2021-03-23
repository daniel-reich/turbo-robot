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
  c = Counter(s)
  return sum(l-l%2 for l in c.values()) + any(l%2 for l in c.values())

