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
  x = ''
  txt = txt.replace(' ', '  ')
  for i in range(len(txt)):
    if i % 2 == 0:
      x += txt[i].upper()
    else:
      x += txt[i].lower()
  return x.replace('  ', ' ')

