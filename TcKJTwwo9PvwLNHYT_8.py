"""


A palindrome is a word that is identical forward and backwards.

  * mom
  * racecar
  * kayak

Given a word, create a function that checks whether it is a palindrome.

### Examples

    is_palindrome("mom") ➞ True
    
    is_palindrome("scary") ➞ False
    
    is_palindrome("reviver") ➞ True
    
    is_palindrome("stressed") ➞ False

### Notes

All test input is lower cased.

"""

def is_palindrome(txt):
  x = int(len(txt)/2)
  w=[]
  y=[]
  for i in range(0,x):
    w += [ord(txt[i])]
  for i in range(0,x):
    txt1 = txt[::-1]
    y += [ord(txt1[i])]
  if sum(w) == sum(y):
    return True
  else:
    return False

