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
  if not 'a' in txt and txt!='':return eval(txt.replace('=','=='))
  if 'a' in txt:
    txt=txt.split('=');a=1
    while eval(txt[1])!=eval(txt[0]):
      mem=abs(eval(txt[1])-eval(txt[0]));a+=1
      if abs(eval(txt[1])-eval(txt[0]))>mem:break
    return eval(txt[1])==eval(txt[0])

