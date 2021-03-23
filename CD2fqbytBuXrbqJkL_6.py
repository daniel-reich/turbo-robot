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
    l1 =  [a for a in txt1.replace(' ', '')]
    l2 =  [a for a in txt2.replace(' ', '')]
    try:
        for i in l1[:]:
            if i in l2:
                l2.remove(i)
                l1.remove(i)
        return len(l1) == 0
    except:
        return False

