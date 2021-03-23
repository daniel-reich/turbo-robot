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

def longest_palindrome(s):
  res = {}
  for i in range(len(s)):
    item = s[i]
    if item in res:
      res[item] += 1
    else:
      res[item] = 1
  uniques = len([i for i in list(res.values()) if i % 2])
  return len(s) if uniques <= 1 else len(s) - uniques + 1

