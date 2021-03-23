"""


Given the parameters day, month and year, return whether that date is **a
valid date**.

### Examples

    is_valid_date(35, 2, 2020) ➞ False
    # February doesn't have 35 days.
    
    is_valid_date(8, 3, 2020) ➞ True
    # 8th March 2020 is a real date.
    
    is_valid_date(31, 6, 1980) ➞ False
    # June only has 30 days.

### Notes

Try using the `datetime` module to complete this challenge (see the
**Resources** tab for some tutorials on this).

"""

def is_valid_date(d, m, y):
  if not 0<m<13 or not 0<d<32: #false case
    return False
  elif m==2: #february
    return d<29 or (d==29 and y%4==0)
  else:#rest
    return d<31 or (d==31 and m in [1,3,5,7,8,10,12])

