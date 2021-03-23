"""


  * "coconuts" has 8 letters.
  * A byte in binary has 8 bits.
  * A byte can represent a character.

We can use the word "coconuts" to communicate with each other in binary if we
use upper case letters as 1s and lower case letters as 0s.

 **Create a function that translates a word in plain text, into Coconut.**

###  Worked Example

    The binary for "coconuts" is
    01100011 01101111 01100011 01101111 01101110 01110101 01110100 01110011
    c         o        c       o       n        u        t       s
    
    Since 0s are lowercase and 1s are uppercase, we can map the binary like this.
    cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS
    
    coconut_translator("coconuts") ➞ "cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS"

### Examples

    coconut_translator("Hi") ➞ "cOcoNuts cOCoNutS"
    
    coconut_translator("edabit") ➞ "cOConUtS cOConUts cOConutS cOConuTs cOCoNutS cOCOnUts"
    
    coconut_translator("123") ➞ "coCOnutS coCOnuTs coCOnuTS"

### Notes

  * All inputs will be strings.
  * Make sure to separate the _coconuts_ with spaces.

"""

def coconut_translator(txt):
    ans = list(map(lambda x:bin(ord(x))[2:].rjust(8,'0'),list(txt)))
    def c(x):
        t = list('coconuts')
        ans = ''.join(list(map(lambda y: t.pop(0).upper() if y == '1' else t.pop(0), x)))
        t = list('coconuts')
        return ans
    return ' '.join(list(map(lambda x:c(x),ans)))

