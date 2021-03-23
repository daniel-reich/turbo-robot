"""


Given a **two digit** number, return `True` if that number contains **one
even** and **one odd** digit.

### Examples

    one_odd_one_even(12) ➞ True
    
    one_odd_one_even(55) ➞ False
    
    one_odd_one_even(22) ➞ False

### Notes

N/A

"""

def one_odd_one_even(n):
  nlist = list(str(n))
  even = 0
  for x in nlist:
    if int(x) % 2 == 0:
      even+=1
    else:
      continue  
  if even == 1:
    return True
  else:
    return False

