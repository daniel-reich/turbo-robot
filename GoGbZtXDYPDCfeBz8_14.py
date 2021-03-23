"""


You are to read each part of the date into its own integer type variable. The
year should be a 4 digit number. You can assume the user enters a correct date
(no error checking required).

Determine whether the entered date is a _magic date_. Here are the rules for a
magic date:

  * `mm * dd` is a 1-digit number that matches the last digit of `yyyy` _or_
  * `mm * dd` is a 2-digit number that matches the last 2 digits of `yyyy` _or_
  * `mm * dd` is a 3-digit number that matches the last 3 digits of `yyyy`

The program should then display `True` if the date is magic, or `False` if it
is not.

### Examples

    magic("1 1 2011") ➞ True
    
    magic("4 1 2001") ➞ False
    
    magic("5 2 2010") ➞ True
    
    magic("9 2 2011") ➞ False

### Notes

N/A

"""

def magic(txt):
  lst = txt.split()
  day_month = int(lst[0]) * int(lst[1])
  last_1 = int(lst[2][-1])
  last_2 = int(lst[2][2:])
  last_3 = int(lst[2][3:])
  if day_month == (last_1 or last_2 or last_3):
    return True
  else:
    return False

