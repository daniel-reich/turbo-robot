"""


An _authentic_ vowel skewer is a skewer with a delicious and juicy mix of
consonants and vowels. However, the way they are made must be _just right_ :

  * Skewers must begin and end with a **consonant**.
  * Skewers must **alternate** between consonants and vowels.
  * There must be an **even spacing** between each letter on the skewer, so that there is a consistent flavour throughout.

Create a function which returns whether a given vowel skewer is **authentic**.

### Examples

    is_authentic_skewer("B--A--N--A--N--A--S") ➞ True
    
    is_authentic_skewer("A--X--E") ➞ False
    # Should start and end with a consonant.
    
    is_authentic_skewer("C-L-A-P") ➞ False
    # Should alternate between consonants and vowels.
    
    is_authentic_skewer("M--A---T-E-S") ➞ False
    # Should have consistent spacing between letters.

### Notes

  * All tests will be given in uppercase.
  * Strings without any actual skewer `"-"` or letters should return `False`.

"""

def is_authentic_skewer(st):
    lst=[i for i in st]
    if lst[0].lower() and lst[-1].lower() not in "bcdfghjklmnpqrstvwxyz" or "-" not in lst: return False
    dashcount=0
    for n in range(1,len(lst)):
        if lst[n].isalpha()==False:dashcount+=1
        else:break
    lss=[lst[i] for i in range(0,len(lst),dashcount+1)]
    if '-' in lss or not all([lss[i].lower() not in "aeiou" for i in range(0,len(lss),2)]) or not all([lss[i].lower() in "aeiou" for i in range(1,len(lss),2)]):return False
    return True

