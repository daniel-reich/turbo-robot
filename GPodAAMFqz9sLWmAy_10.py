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
  temp = str(n)
  indiv = list(temp)
  odd = 0
  even = 0
  for val in indiv:
    if int(val) % 2 != 0 and int(val) != 0:
      odd += 1
    elif int(val) % 2 == 0:
      even += 1
  if even == 1 and odd == 1:
    return True
  else:
    return False

