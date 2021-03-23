"""


In **Paul Cipher** , only alpha characters will be encoded with the following
rules:

  * All alpha characters will be treated as uppercase letters.
  * The first alpha character will not change (except for switching to upper case).
  * All subsequent alpha characters will be shifted toward "Z" by the alphabetical position of the previous alpha character (wrap back to "A" if "Z" is passed).

`he1lo` would be encoded as follows:

    paul_cipher("he1lo") ➞ "HM1QA"
    
    h -> H (First character to be changed to uppercase)
    e -> M (H is the previous alpha character and 8th letter in the alphabets. E + 8 = M)
    1 -> 1 (Keep all characters other than alphabets as it is)
    l -> Q (E is the previous alpha character and 5th letter in the alphabets. L + 5 = Q)
    o -> A (L is the previous alpha character and 12th letter in the alphabets. O + 12 = A)

Given a string `txt`, return the encoded message. See the below examples for a
better understanding:

### Examples

    paul_cipher("muBas41r") ➞ "MHWCT41K"
    
    paul_cipher("a1rForce") ➞ "A1SXUGUH"
    
    paul_cipher("MATT") ➞ "MNUN"

### Notes

N/A

"""

def paul_cipher(txt):
    myans = ''
    for i in range(len(txt)):
        if txt[i].isalpha():
            myans += txt[i].upper()
            ctr = ord(txt[i].upper())-64
            break
        else:
            myans += txt[i]
    i += 1
​
    for j in range(i,len(txt)):
        if txt[j].isalpha():
            myans += chr((((ord(txt[j].upper())-64) + ctr-1) % 26)+65)
            ctr = ord(txt[j].upper())-64
        else:
            myans += txt[j]
​
    return myans

