"""


Given a range of years as a string, return the **number of leap years** there
are within the range (inclusive).

### Examples

    num_of_leapyears("1980-1984") ➞ 2
    # 1980 and 1984 are leapyears.
    
    num_of_leapyears("2000-2020") ➞ 6
    
    num_of_leapyears("1600-2000") ➞ 98

### Notes

  * Remember that a _hyphen_ separates the years.
  * Check the **Resources** tab for help on checking whether a year is a leap year.

"""

import calendar
def num_of_leapyears(years):
  y = list(map(int,years.split("-")))
  k = 0
  
  for i in range(y[0],y[1]+1, 1):
    if (calendar.isleap(i)):
      k += 1
  return k

