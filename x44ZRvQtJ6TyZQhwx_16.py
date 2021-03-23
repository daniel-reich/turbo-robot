"""


A **pandigital** number contains all digits (0-9) at least once. Write a
function that takes an integer, returning `True` if the integer is pandigital,
and `False` otherwise.

### Examples

    is_pandigital(98140723568910) ➞ True
    
    is_pandigital(90864523148909) ➞ False
    # 7 is missing.
    
    is_pandigital(112233445566778899) ➞ False

### Notes

Think about the properties of a pandigital number when all duplicates are
removed.

"""

def is_pandigital(n):
  a=[]
  while(n>0):
    b=n%10
    a.append(b)
    n=n//10
  s=set(a)
  l=list(s)
  e=[0,1,2,3,4,5,6,7,8,9]
  
  if l==e:
    return True
  else :
    return False

