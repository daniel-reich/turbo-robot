"""


 _lPaeesh le pemu mnxit ehess rtnisg!_ Oh, sorry, that was supposed to say:
_Please help me unmix these strings!_

Somehow my strings have all become mixed up; every pair of characters has been
swapped. Help me undo this so I can understand my strings again.

### Examples

    unmix("123456") ➞ "214365"
    
    unmix("hTsii  s aimex dpus rtni.g") ➞ "This is a mixed up string."
    
    unmix("badce") ➞ "abcde"

### Notes

The length of a string can be odd — in this case the last character is not
altered (as there's nothing to swap it with).

"""

def unmix(txt):
  li=list() 
  for i in range(0,len(txt)-1,2):
    for j in range(i+1,len(txt),2):
      li.append(txt[j])
      break
    li.append(txt[i])
  if(len(txt)%2!=0):
    li.append(txt[-1])
  return (''.join(li))

