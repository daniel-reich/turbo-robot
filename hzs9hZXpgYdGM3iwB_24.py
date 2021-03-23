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
  new_txt=''
  caps=True
  for i in txt:
    if i.isalpha():
      if caps:
        new_txt+=i.upper()
        caps=False
      else:
        new_txt+=i.lower()
        caps=True
    else: new_txt+=i
  return new_txt

