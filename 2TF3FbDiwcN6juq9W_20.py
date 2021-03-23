"""


Given a `date`, return how many days `date` is away from 2021 (end date not
included). `date` will be in **mm/dd/yyyy** format.

### Examples

    days_until_2021("12/28/2020") ➞ "3 days"
    
    days_until_2021("1/1/2020") ➞ "366 days"
    
    days_until_2021("2/28/2020") ➞ "308 days"

### Notes

All given dates will be in the year 2020.

"""

from datetime import datetime, date, timedelta
​
def days_until_2021(t1):
  a = "days"
  t1 = datetime.strptime(t1, '%m/%d/%Y')
  t2 = datetime(2021, 1, 1)
  if (t2-t1).days == 1:
    a = "day"
  return '{} {}'.format((t2-t1).days, a)

