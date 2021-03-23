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
    x,y,res=[],[],''
    d={0:'c',1:'o',2:'c',3:'o',4:'n',5:'u',6:'t',7:'s'}
    txt1=bytearray(txt, "utf8")
    for i in txt1:
        i=bin(i)
        if len(i)==9:
            a=i.replace('b','')
        else:
            a=i.replace('b','0')
        x.append(a)
    for i in x:
        for j,v in enumerate(i):
            if j in d:
                if v=='0':
                    res+=d[j]
                else:
                    res+=d[j].upper()
        y.append(res)
        res=''
    return ' '.join(y)

