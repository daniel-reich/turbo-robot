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

import re
def day_of_year(date):
  nums = re.findall(r'\d+',date)
  m,d,y = int(nums[0]),int(nums[1]),int(nums[2])
  days = [31,28,31,30,31,30,31,31,30,31,30,31]
  if m == 1:
    return d
  if m == 2:
    return 31 + d
  if y % 4 == 0:
    if y % 100 == 0:
      if y % 400 == 0:
        days[1] = 29
    else:
      days[1] = 29
  return sum(days[:m-1]) + d

