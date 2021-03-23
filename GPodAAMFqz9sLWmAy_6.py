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
  o = len([i for i in str(n) if int(i) % 2 != 0])
  e = len([i for i in str(n) if int(i) % 2 == 0])
  return o == e

