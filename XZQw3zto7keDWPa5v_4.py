"""


Create a function that takes the month and year (as integers) and returns the
number of days in that month.

### Examples

    days(2, 2018) ➞ 28
    
    days(4, 654) ➞ 30
    
    days(2, 200) ➞ 28
    
    days(2, 1000) ➞ 28

### Notes

Don't forget about leap years!

"""

def day_amount(month, year):
  from calendar import monthrange
  tupla = monthrange(year,month)
  return tupla[1]

