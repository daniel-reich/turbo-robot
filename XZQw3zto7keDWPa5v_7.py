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
  if month == 2:
    return 29 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 28
  return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30

