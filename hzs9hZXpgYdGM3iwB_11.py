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
  s=list(txt.replace(" ",""))
  for i in range(len(s)):
    if i%2==0:
      s[i]=s[i].upper()
    else: s[i]=s[i].lower()
  x=[index for index,val in enumerate(txt) if val==" "]
  for num in x:
    s.insert(num," ")
  return "".join(s)

