"""


Create a function that determines whether it is possible to build a palindrome
from the characters in a string.

### Examples

    possible_palindrome("acabbaa") ➞ True
    # Can make the following palindrome: "aabcbaa"
    
    possible_palindrome("aacbdbc") ➞ True
    # Can make the following palindrome: "abcdcba"
    
    possible_palindrome("aacbdb") ➞ False
    
    possible_palindrome("abacbb") ➞ False

### Notes

N/A

"""

def countin(txt, a):
  b=0
  for i in txt:
    if i == a:
      b += 1
  return(b)
​
def possible_palindrome(txt):
  a = 0
  for i in txt: 
    if countin(txt, i)%2 != 0:
      a += 1/countin(txt, i)
  return(a <= 1)

