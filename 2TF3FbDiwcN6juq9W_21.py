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

import datetime
def days_until_2021(date):
  parts = date.split('/')
  current = datetime.date(int(parts[2]),int(parts[0]),int(parts[1]))
  new_year = datetime.date(2021,1,1)
  delta = new_year - current
  return str(delta.days) + ' days' if delta.days > 1 else str(delta.days) + ' day'

