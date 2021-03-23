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

def can_build(word1,word2):
  s=[]
  for i in ''.join(word1.split()):
    s.append(i in ''.join(word2.split()))
    print(s)
    word2=word2.replace(i,"",1)
  return min(s)!=False

