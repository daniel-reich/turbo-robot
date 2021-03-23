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
  u, ui = '', 0
  for i in txt:
    if i.isalpha():
      if ui == 0:
        u += i.upper()
      else:
        u += i.lower()
      ui = (ui + 1) % 2
    else:
      u += i
  return u

