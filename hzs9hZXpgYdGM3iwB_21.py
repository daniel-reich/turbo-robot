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
  
  words = txt.split()
  cap = True
  new_words =[]
  
  for word in words:
    newword = ''
    for l8r in word:
      if cap == True:
        newword += l8r.upper()
        cap = False
      elif cap == False:
        newword += l8r.lower()
        cap = True
    new_words.append(newword)
  
  return ' '.join(new_words)

