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
  new = []
  if len(txt1)<=len(txt2):
    d1 = {i: txt1.count(i) for i in sorted(txt1.replace(' ', ''))}
    d2 = {i: txt2.count(i) for i in sorted(txt2.replace(' ', ''))}
    for i in d1:
      if d1[i] <= d2[i]:
        new.append(i)
    if len(d1) == len(new):
      return True
    else:
      return False
  else:
    return False

