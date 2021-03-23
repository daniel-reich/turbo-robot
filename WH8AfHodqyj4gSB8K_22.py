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

def is_authentic_skewer(s):
    v = ["A","E","I","O","U"]
    c = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
    if s[0] not in c or s[len(s)-1] not in c:
            #print("Beginning and end are not Consonents")
            return False
    nd=[x for x in s if x != "-"]
    for i in range(len(nd)-1):
        if (nd[i] in v and nd[i+1] in v) or (nd[i] in c and nd[i+1] in c):
            #print("No alternation between consonents and vowels")
            return False
    
    sp=s.index(nd[1])-s.index(nd[0])
    for i in range(0,len(s)-3,sp):
        if s[i] not in v and s[i] not in c:
            #print("Spacing Issue")
            return False
    return True

