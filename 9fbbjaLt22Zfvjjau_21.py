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

def paul_cipher(s):
    w = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    fl = ''
    for letter in s:
        if not fl and letter.isalpha():
            fl = True
            result+=letter
            n = w.index(letter.lower())+1
        elif letter.isalpha():
            r =  (n+ w.index(letter.lower())+1)
            result = result + w[(r-26)-1 if r >= 26 else r-1] 
            n = w.index(letter.lower())+1
        else:
            result+=letter
    return result.upper()

