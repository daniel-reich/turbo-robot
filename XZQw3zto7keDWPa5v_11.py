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
  if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    return 29
  elif month == 2:
    return 28
  elif month != 2 and month % 2 == 0 and month < 7:
    return 30
  elif (month != 2 and month % 2 == 0 and month > 7) or (month % 2 != 0 and month <= 7):
    return 31
  else:
    return 30

