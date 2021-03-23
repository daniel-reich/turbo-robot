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
  m,d,y = [int(p) for p in date.split('/')]
​
  ms = [31,28,31,30,31,30,31,31,30,31,30,31]
  
  ys = ((y%4==0) - (y%100==0) + (y%400==0)) and m > 2
  
  return d + sum(ms[:m-1]) + ys

