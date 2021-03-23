"""


Create a function that takes a word and returns `True` if the word has two
consecutive identical letters.

### Examples

    double_letters("loop") ➞ True
    
    double_letters("yummy") ➞ True
    
    double_letters("orange") ➞ False
    
    double_letters("munchkin") ➞ False

### Notes

N/A

"""

def double_letters(word):
  a = list(word)
  n = len(word)
  for i in range(0,n-1):
    if a[i]==a[i+1]:
      return True
      exit
  return False

