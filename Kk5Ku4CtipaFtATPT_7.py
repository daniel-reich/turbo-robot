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
    coco = "coconuts"
    trans = lambda char: "".join([coco[ix] if ch == '0' else coco[ix].upper() \
    for ix, ch in enumerate([bd for bd in bin(ord(char))[2:].zfill(8)])])
    return " ".join(trans(ch) for ch in txt)

