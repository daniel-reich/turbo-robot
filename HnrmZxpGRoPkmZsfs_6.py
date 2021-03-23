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
  if m>12:
    return False
  if ( m==4 or m==6 or m==9 or m==11):
    if d>30:
      return False
    else:
      return True
  if m==2:
    if d>29:
      return False
    elif d>28:
      if (y%400==0 or y%4==0):
        if(y%100==0):
          return False
        else:
          return True
      return False
    return True
  elif d>31:
    return False
  else:
    return True

