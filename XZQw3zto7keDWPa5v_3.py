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
  Calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if (month != 2):
    return Calendar[month-1]
  elif (month == 2 and year%4 != 0):
    return Calendar[1]
  elif (month == 2 and year%100 != 0):
    return Calendar[1]+1
  elif (month == 2 and year%400 != 0):
    return Calendar[1]
  else:
    return Calendar[1]+1

