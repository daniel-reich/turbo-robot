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
  l = list(str(n))
  n1 = 0
  for i in range(0,len(l)):
    if int(l[i]) % 2 == 0:
      n1 += 1
  if n1 == 1:
    return True
  else:
    return False

