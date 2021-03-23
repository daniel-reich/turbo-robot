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
  b = str(n)
  return int(b[0]) % 2 == 0 and int(b[1]) % 2 == 1 or int(b[0]) % 2 == 1 and int(b[1]) % 2 == 0

