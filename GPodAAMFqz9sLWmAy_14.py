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
  a = list(str(n))
  odd,even = 0,0
  for i in a:
    if int(i) % 2 == 0:
      even = even + 1
    else:
      odd = odd + 1
  if odd == even:
    return True
  else:
    return False

