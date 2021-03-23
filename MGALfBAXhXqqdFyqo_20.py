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

a = [chr(i) for i in range(ord('a'),ord('z')+1)]
b = [chr(i) for i in range(ord('A'),ord('Z')+1)]
​
def atbash(txt):
    g = []
    for z in txt:
        if z.isupper() == True:
            g.append(chr(65+(abs(ord(chr(90-ord(z)))))))
        if z.islower() == True:
            g.append(chr(97 + (abs(ord(chr(122 - ord(z)))))))
        elif not z.isalpha() == True:
            g.append(z)
    return("".join(g))

