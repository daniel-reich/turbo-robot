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
  d = dict([[i,s.count(i)] for i in s])
  ret = 0
  for i in d:
    if ret==0 and any([d[j]%2==1 for j in d]):
      ret+=1
    if d[i]>=2:
      ret+=(d[i]//2)*2
  return ret if s else 0

