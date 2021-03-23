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

import string
def paul_cipher(txt):
    output = ""
    firstalpha = True
    letters = string.ascii_lowercase
    for i in range(len(txt)):
        if txt[i].isalpha() and firstalpha:
            output += txt[i].upper()
            firstalpha = False
            prevletterindex = letters.index(txt[i].lower())
        elif txt[i].isalpha():
            ciphindex = letters.index(txt[i].lower()) + prevletterindex + 1
            if ciphindex >= 26:
                ciphindex -= 26
            output += letters[ciphindex].upper()
            prevletterindex = letters.index(txt[i].lower())
        else:
            output += txt[i]
    return output

