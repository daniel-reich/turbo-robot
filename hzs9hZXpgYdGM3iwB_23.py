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

def alternating_caps(txt):
    str_new, ind ='', 0
    for i in range(len(txt)):
        if ind == 0 and txt[i] != ' ':
            str_new = str_new + txt[i].upper()
            ind = 1
        elif ind == 1 and txt[i] != ' ':
            str_new = str_new + txt[i].lower()
            ind = 0
        else:
            str_new= str_new + ' '
            continue
    return str_new

