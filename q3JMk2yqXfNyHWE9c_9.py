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

def double_letters(w):
  t=0
  c=w[0]
  for l in w+' ':
    if c==l:
      t+=1
    else:
      if t==2:
        return True
      c=l
      t=1
  return False

