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
  mdays = [31,28,31,30,31,30,31, 31,30,31,30,31]
  m, d, y = map(int, date.split('/'))
  isLeap = y%4==0 and (y%100!=0 or y%400==0)
  return sum(mdays[:m-1]) + d + (1 if isLeap and m > 2 else 0)

