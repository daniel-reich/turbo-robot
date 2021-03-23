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

def with_a(txt):
  for a in range(1,100):
    lst = txt.split('=')
    for i in range(len(lst)-1):
      if eval(lst[i]) == eval(lst[i+1]):
        return True
  return False
  
def no_a(txt):
  lst = txt.split('=')
  for i in range(len(lst)-1):
    if eval(lst[i]) != eval(lst[i+1]):
      return False
  return True       
​
def formula(txt):
  return with_a(txt) if 'a' in txt else None if not len(txt) else no_a(txt)

