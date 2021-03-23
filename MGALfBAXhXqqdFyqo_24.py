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
  temp = ""
  for char in txt:
    if 65 <= ord(char) <= 90:
      char = 65 + (90 - ord(char))
      temp += chr(char) 
    elif 97 <= ord(char) <= 122:
      char = 97 + (122 - ord(char))
      temp += chr(char) 
    else:
      temp += char
  return temp

