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
  # september(9), april(4), june(6) and november(11)
  thirty = [4, 6, 9, 11]
  if month == 2:
    if (year%4==0 and year%100 != 0) or (year%100==0 and year%400==0):
      days = 29 
    else: 
      days = 28
  elif month in thirty:
    days = 30 
  else:
    days = 31
  return days

