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
  uc,lc = list(range(ord('A'), ord('Z')+1)), list(range(ord('a'), ord('z')+1))
  normal = [chr(i) for i in uc]+[chr(i) for i in lc]
  cipher = [chr(i) for i in uc[::-1]]+[chr(i) for i in lc[::-1]]
  return ''.join(cipher[normal.index(i)] if i.isalpha() else i for i in txt)

