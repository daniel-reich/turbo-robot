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
    upper = True
    result = ''
    for x in txt:
        if x.isalpha():
            if upper == True:
                result += x.upper()
                upper = False
            else:
                result += x.lower()
                upper = True
        else:
            result += x
    return result

