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
  count = 0
  mystr = ""
  for i in range (len(txt)):
    if (count%2==0 and txt[i]!=" "):
      mystr += txt[i].upper()
      count += 1
    elif (count%2!=0 and txt[i]!=" "):
      mystr += txt[i].lower()
      count += 1
    elif (txt[i]== " "):
      mystr += txt[i]
  return mystr

