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
  return all(abs(ord(x) - ord(y)) == 1 and abs(ord(z) - ord(y)) == 1  \
    for x,y,z in zip(txt, txt[1:], txt[2:]))

