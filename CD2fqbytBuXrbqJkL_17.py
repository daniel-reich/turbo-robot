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
  txt1_lst = txt1.split()
  txt2_lst = txt2.split()
  txt1 = "".join(txt1_lst)
  txt2 = "".join(txt2_lst)
  count = 0
  for char in range(len(txt1)):
    if txt1[char] in txt2:
      count += 1
      txt2 = txt2.replace(txt1[char], "", 1)
  if count == len(txt1):
    return True
  else:
    return False

