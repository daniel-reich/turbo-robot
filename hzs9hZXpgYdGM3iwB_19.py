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
    i, lst = 0, []
    for x in txt.split():
        s = ''
        for ch in x:
            if not i%2:
                s+=ch.upper()
            else:
                s+=ch.lower()
            i+=1
        lst.append(s)
​
    return ' '.join(lst)

