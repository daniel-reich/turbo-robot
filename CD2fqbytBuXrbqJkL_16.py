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
  canBuild = False
  txt2 = txt2.split(" ")
  for word in txt2:
      if len(word) > 0:
          for i in word:
              if i in txt1:
                  word = word.replace(i, "", 1)
                  txt1 = txt1.replace(i, "", 1)
  for i in txt1:
      if i == " ":
          txt1 = txt1.replace(" ", "")
  if len(txt1) == 0:
      canBuild = True
​
  return canBuild

