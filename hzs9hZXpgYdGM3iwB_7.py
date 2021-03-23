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
  is_cap = True
  new_txt = ""
  for letter in txt:
    if letter != " ":
      if is_cap:
        new_txt += letter.upper()
        is_cap = False
      else:
        new_txt += letter.lower()
        is_cap = True
    else:
      new_txt += " "
  return new_txt

