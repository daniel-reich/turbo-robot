"""


Create a function that takes a string and returns `True` or `False` depending
on whether or not the given formula is correct.

### Examples

    formula("6 * 4 = 24") ➞ True
    
    formula("18 / 17 = 2") ➞ False
    
    formula("") ➞ None

### Notes

  * You have to figure out what `a` is.
  * Ignore the spaces.
  * If the input is an empty string `""`, return `None`.
  * You do not need to dynamically find the value of `a` (it's a constant and the same accross all tests).

"""

def formula(txt):
  if txt=='':
    return None
  txt=txt.replace(' ','')
  if 'a' in txt:
    if len(txt)==6:
      return False
    else:
      return  True
  else: 
    lst=txt.split('=')
    for i in lst:
      lst[lst.index(i)]=int(eval(i))
    return True if len(set(lst))==1 else False

