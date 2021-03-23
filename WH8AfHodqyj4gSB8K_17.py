"""


An _authentic_ vowel skewer is a skewer with a delicious and juicy mix of
consonants and vowels. However, the way they are made must be _just right_ :

  * Skewers must begin and end with a **consonant**.
  * Skewers must **alternate** between consonants and vowels.
  * There must be an **even spacing** between each letter on the skewer, so that there is a consistent flavour throughout.

Create a function which returns whether a given vowel skewer is **authentic**.

### Examples

    is_authentic_skewer("B--A--N--A--N--A--S") ➞ True
    
    is_authentic_skewer("A--X--E") ➞ False
    # Should start and end with a consonant.
    
    is_authentic_skewer("C-L-A-P") ➞ False
    # Should alternate between consonants and vowels.
    
    is_authentic_skewer("M--A---T-E-S") ➞ False
    # Should have consistent spacing between letters.

### Notes

  * All tests will be given in uppercase.
  * Strings without any actual skewer `"-"` or letters should return `False`.

"""

from collections import Counter
def is_authentic_skewer(n):
  v=["A","E","I","O","U"]
  z=n.replace("-","")
  if(len(z)<2):
    return False
  i=0
  step=list()
  c=0
  i=0
  while(i<len(n)):
    if((i==0 or i==len(n)-1) and n[i] in v):
      return False
    elif(n[i]=='-'):
      j=i
      while(j<len(n) and n[j]=='-'):
        j+=1
      step.append(j-i)
      i=j   
    elif(c==0 and n[i] not in v):
      c=1
      i+=1
    elif(c==1 and n[i] in v):
      c=0
      i+=1
    elif(c==0 and n[i] in v):
      return False
    elif(c==1 and n[i] not in v):
      return False
  if(len(Counter(step))!=1):
    return False
  return True

