"""


A leap year happens every four years, so it's a year that is perfectly
divisible by four. However, if the year is a multiple of 100 (1800, 1900,
etc), the year must be divisible by 400.

Write a function that determines if the year is a leap year or not.

### Examples

    leap_year(2020) ➞ True
    
    leap_year(2021) ➞ False
    
    leap_year(1968) ➞ True

### Notes

N/A

"""

def leap_year(year):
  total = year % 4 == 0
  total1 = total % 100 == 0
  if total == False:
    return False
  else:
    return True

