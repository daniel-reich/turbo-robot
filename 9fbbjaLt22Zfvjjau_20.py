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
    char_alpha = [chr(i) for i in range(65, 91)]
    num = [chr(i) for i in range(48, 58)]
    char = [chr(i) for i in range(33, 48)]
    char2 = ["{", "|", "}", "~"]
    char.extend(char2)
    idx_previous = []
    sifra = []
    j = 0
    idx = []
    first_is_num = False
    for i in txt:
        first_is_num = False
        if txt.index(i) == 0:
            if i in num:
                sifra.append(i)
                first_is_num = True
            else:
                sifra.append(i.upper())
            if i.upper() in char_alpha:
                idx_previous.append(char_alpha.index(i.upper()))
​
        if i.upper() in char_alpha and txt.index(i) != 0 and first_is_num != True:
            idx = char_alpha.index(i.upper())
            if idx_previous != []:
                idx += idx_previous[j] + 1
                j += 1
            idx %= len(char_alpha)
            sifra.append(char_alpha[idx])
            idx_previous.append(char_alpha.index(i.upper()))
​
        if i in num and first_is_num != True:
            sifra.append(i)
​
        if i in char and first_is_num != True:
            sifra.append(i)
​
​
    return "".join(i for i in sifra)

