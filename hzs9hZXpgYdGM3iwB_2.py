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
  txt = txt.lower()
  res = ""
  i=0
  for ch in txt:
    if ch.isalpha():
      if i%2==0: res += ch.upper()
      else:      res += ch.lower()
      i+=1
    else:
      res += ch
  return res

