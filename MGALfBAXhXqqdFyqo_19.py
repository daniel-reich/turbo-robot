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
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  ret = ''
  i = 0
  for char in txt:
    if char.isalpha():
      if char.isupper():
        ret = ret + alpha[-(alpha.index(char.lower())+1)].upper()
      else:
        ret = ret + alpha[-(alpha.index(char)+1)]
    else:
      ret = ret + char
  return ret

