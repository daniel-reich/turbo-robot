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
  """Scrappy, shit code"""
  ans = txt[0].upper()
  for x in range(1,len(txt)): 
    if ans[x-1] == ' ':
      if ans[x-2].isupper() == True:
        ans += txt[x].lower()
      else:
        ans += txt[x].upper()
    elif ans[x-1].isupper() == True:  
      ans += txt[x].lower()
    else:
      ans += txt[x].upper()
  return ans

