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
  x=[]
  for i in range(0,len(txt),2):
    x.append(txt[i])
  y=[]
  for i in range(1,len(txt),2):
    y.append(txt[i])
  if len(x)<len(y):
    x.append('')
  if len(x)>len(y):
    y.append('')    
  c=[]
  for i in range(len(x)):
    c.append(y[i]+x[i])
  return ''.join(c)

