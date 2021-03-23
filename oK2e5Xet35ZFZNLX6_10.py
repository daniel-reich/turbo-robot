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
  
  Code = "abcdefghijklmnopqrstuvwxyz"
  
  First = 0
  Second = 1
  Length = len(txt)
  
  while (Second < Length):
    
    Item_A = txt[First]
    Item_B = txt[Second]
    
    Place_A = Code.index(Item_A)
    Place_B = Code.index(Item_B)
    
    Span = abs(Place_A - Place_B)
    
    if (Span == 1):
      First += 1
      Second += 1
    else:
      return False
      
  return True

