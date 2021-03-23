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

def isLeapYear(year):
  return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));
​
def day_amount(month, year):
  if (month == 1):
    return 31
  elif (month == 2 and isLeapYear(year) == True):
    return 29
  elif (month == 2):
    return 28
  elif (month == 3):
    return 31
  elif (month == 4):
    return 30
  elif (month == 5):
    return 31
  elif (month == 6):
    return 30
  elif (month == 7):
    return 31
  elif (month == 8):
    return 31
  elif (month == 9):
    return 30
  elif (month == 10):
    return 31
  elif (month == 11):
    return 30
  elif (month == 12):
    return 31

