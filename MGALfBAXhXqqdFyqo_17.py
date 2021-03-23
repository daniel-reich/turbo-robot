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
  al='abcdefghijklmnopqrstuvwxyz'
  alc=al.upper()
  alr=al[::-1]
  alcr=alc[::-1]
  dic1={}
  for i in range(26):
    dic1[al[i]]=alr[i]
  dic2={}
  for j in range(26):
    dic2[alc[j]]=alcr[j]
  final=''
  for  k in txt:
    if k in al:
      final+=dic1[k]
    elif k in alc:
      final+=dic2[k]
    else:
      final+=k
  return final

