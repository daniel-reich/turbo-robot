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

from datetime import datetime as dt, timedelta as td, time as t
def day_of_year(date):
  s=date.split('/')
  d1=dt.strptime(date, '%m/%d/%Y')
  d2=dt.strptime('1/'+'1/'+s[-1], '%m/%d/%Y')
  return (d1-d2).days+1

