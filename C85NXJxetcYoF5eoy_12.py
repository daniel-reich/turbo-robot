"""


Create a function that returns how often it has been called previously (i.e.
return the count value _pre-increment_ ).

### Examples

    counter() ➞ 0
    
    counter() ➞ 1
    
    counter() ➞ 2
    
    counter() ➞ 3

### Notes

A global variable is needed for this task.

"""

x=0
​
def counter():
  global x
  t = x
  x += 1
  return t

