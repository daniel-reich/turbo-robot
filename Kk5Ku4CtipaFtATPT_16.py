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

def coconut_translator(s):
    letter = "coconuts"
    bins = ' '.join((8-len(format(ord(item),'b'))) * '0'+ format(ord(item),'b') 
                    if len(format(ord(item),'b')) != 8 else format(ord(item),'b') for item in s).split()
    result =''.join([letter[i] if nums[i] == '0' else letter[i].upper() for nums in bins for i in range(8) ])
    return ' '.join(result[i:i+8] for i in range(0,len(result),8))

