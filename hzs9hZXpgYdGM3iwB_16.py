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
  cnter = 0
  out = ""
  for letter in txt:
    if not letter == ' ':
      cnter += 1
    
    if cnter % 2 != 0:
      out += letter.upper()
    else:
      out += letter.lower()
      
  return out

