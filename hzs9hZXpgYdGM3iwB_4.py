"""


Create a function that alternates the case of the letters in a string (known
as **Spongecase** ).

### Examples

    alternating_caps("Hello") ➞ "HeLlO"
    
    alternating_caps("How are you?") ➞ "HoW aRe YoU?"
    
    alternating_caps("OMG this website is awesome!") ➞ "OmG tHiS wEbSiTe Is AwEsOmE!"

### Notes

  * The first letter should always be UPPERCASE.
  * Ignore spaces.

"""

import string
def alternating_caps(txt):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    count = 0
    x = txt.split(' ')
    x[0] = x[0].capitalize()
    newlist = []
    emptystring = ''
    for eachword in x:
        for eachletter in eachword:
            if eachletter in lowercase and count == 1:
                emptystring += eachletter.upper()
                count = 0
            elif eachletter in lowercase and count == 0:
                count = 1
                emptystring += eachletter
            else:
                emptystring += eachletter
                count = 0
        newlist.append(emptystring)
        emptystring = ''
    return ' '.join(newlist)

