"""


Create a function that takes a string and checks if every single character is
**preceded and followed** by a character adjacent to it in the _english
alphabet_.

Example: "b" should be preceded and followed by ether "a" or "c" (`abc || cba
|| aba || cbc == True` but `abf || zbc == False`).

### Examples

    neighboring("aba") ➞ True
    
    neighboring("abcdedcba") ➞ True
    
    neighboring("efghihfe") ➞ False
    
    neighboring("abc") ➞ True
    
    neighboring("qrstuv") ➞ True
    
    neighboring("mnopqrtstrqpomn") ➞ True

### Notes

All test cases will consist of lower case letters only.

"""

def neighboring(txt):
  for i, j in zip(txt, txt[1:]):
    if abs(ord(i) - ord(j)) != 1:
      return False
  return True

