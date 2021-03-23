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
  dateDict = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
  if month in dateDict:
    return dateDict[month]
  elif (year % 400 == 0) and (year % 100 == 0):
    return 29
  elif year % 4 == 0:
    if year % 100 != 0:
      return 29
    else:
      return 28
  else:
    return 28

