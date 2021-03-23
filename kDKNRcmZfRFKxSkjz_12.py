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
  new_txt=''
  if len(txt)%2==0:
    for i in range(len(txt)):
      if i%2==0:
        new_txt+=txt[i+1]
        new_txt+=txt[i]
  elif len(txt)%2>0:
    for i in range(len(txt)-1):
      if i%2==0:
        new_txt+=txt[i+1]
        new_txt+=txt[i]
    new_txt+=txt[-1]
  return new_txt

