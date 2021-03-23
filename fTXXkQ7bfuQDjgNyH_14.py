"""


Each year has 365 or 366 days. Given a string `date` representing a Gregorian
calendar date formatted as `month/day/year`, return the _day-number_ of the
year.

### Examples

    day_of_year("11/16/2020") ➞ 321
    
    day_of_year("1/9/2019") ➞ 9
    
    day_of_year("3/1/2004") ➞ 61
    
    day_of_year("12/31/2000") ➞ 366

### Notes

All input strings in tests are valid dates.

"""

def day_of_year(date):
  datelist = date.split('/')
  daylist = []
  totaldays = 0
  year = int(datelist[2])
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    daylist = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  else:
    daylist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
  for i in range(int(datelist[0]) - 1):
    totaldays += daylist[i]
  totaldays += int(datelist[1])
  return totaldays

