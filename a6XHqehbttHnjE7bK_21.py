"""


A repdigit is a positive number composed out of the same digit. Create a
function that takes an integer and returns whether it's a repdigit or not.

### Examples

    is_repdigit(66) ➞ True
    
    is_repdigit(0) ➞ True
    
    is_repdigit(-11) ➞ False

### Notes

  * The number `0` should return `True` (even though it's not a positive number).
  * Check the **Resources** tab for more info on repdigits.

"""

def is_repdigit(num):
  if num<0:
    return False
  
  a=[]
  while(num>0):
    b=num%10
    num=num//10
    a.append(b)
  c=set(a)
  
  if len(c)==1:
    return True
  return False

