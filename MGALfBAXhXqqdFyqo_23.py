"""


The Atbash cipher is an encryption method in which each letter of a word is
replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X;
etc.

Create a function that takes a string and applies the Atbash cipher to it.

### Examples

    atbash("apple") ➞ "zkkov"
    
    atbash("Hello world!") ➞ "Svool dliow!"
    
    atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"

### Notes

  * Capitalisation should be retained.
  * Non-alphabetic characters should not be altered.

"""

def atbash(txt):
​
  lowerkey = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
  lowerval = reversed(lowerkey)
​
  lv2 = []
​
  for item in lowerval:
    lv2.append(item)
  
  lowerval = lv2
  del lv2
  lower = {}
​
  for n in range(0, len(lowerkey)):
    key = lowerkey[n]
    val = lowerval[n]
​
    lower[key] = val
  
  upperkey = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
  upperval = reversed(upperkey)
​
  uv2 = []
​
  for item in upperval:
    uv2.append(item)
  
  upperval = uv2
  del uv2
  upper = {}
​
  for n in range(0, len(upperkey)):
    k = upperkey[n]
    v = upperval[n]
​
    upper[k] = v
​
  ns = ''
​
  for item in txt:
    if item in upper.keys():
      ns += upper[item]
    elif item in lower.keys():
      ns += lower[item]
    else:
      ns += item
    
  return ns

