"""


Write a function that returns `True` if it's possible to build a phrase `txt1`
using only the characters from another phrase `txt2`.

### Examples

    can_build("got 2 go", "gogogo 2 today") ➞ True
    
    can_build("sit on top", "its a moo point") ➞ True
    
    can_build("long high add or", "highway road go long") ➞ False
    
    can_build("fill tuck mid", "truck falls dim") ➞ False

### Notes

  * All letters will be in lower case.
  * Numbers and special characters included.
  * Ignore whitespaces.
  * Do not count white space as a character.

"""

def can_build(txt1, txt2):
  txt1 = txt1.replace(" ","")
  txt2 = txt2.replace(" ","")
  s1 = set(txt1)
  d1 = {el:txt1.count(el) for el in txt1}
  s2 = set(txt2)
  d2 = {el:txt2.count(el) for el in txt2}
  if s1.issubset(s2):
    for el in txt1:
      if d1[el] > d2[el]:
        return False
    return True
  else:
    return False

