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

import itertools as it
def alternating_caps(txt):
  t   = txt.replace(' ', '')
  alt = [
    l for z in it.zip_longest(
      t[::2].upper(), t[1::2].lower(), fillvalue=''
    ) for l in z
  ]
  return ''.join(c if c == ' ' else alt.pop(0) for c in txt)

