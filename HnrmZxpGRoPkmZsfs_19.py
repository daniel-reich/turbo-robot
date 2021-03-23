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
  months31 = (1, 3, 5, 7, 8, 10, 12)
  months30 = (4, 6, 9, 11)
  if int(d)<33:
    if m == 2 and int(d) < 29:
      return(True)
    for x in months31:
      if int(m) == int(x) and int(d) < 32:
        return(True)
    for x in months30:
      if int(m) == int(x) and int(d) < 31:
        return(True)
  return(False)

