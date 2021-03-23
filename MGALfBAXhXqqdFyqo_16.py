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
  low = "abcdefghijklmnopqrstuvwxyz"
  low_atb = "zyxwvutsrqponmlkjihgfedcba"
​
  NT = ''
  for i in txt:
    if i.islower():
      if i.isalpha():
        inx = low.index(i)
        NT += low_atb[inx]
      else:
        NT += i
    else:
      if i.isalpha():
        inx = low.index(i.lower())
        NT += low_atb[inx].upper()
      else:
        NT += i
  return NT

