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

from datetime import date
def days_until_2021(d):
  a = d.split('/')
  d1 = int(a[2])
  d2 = int(a[0])
  d3 = int(a[1])
  dd1 = date(d1, d2, d3)
  dd2 = date(2021, 1, 1)
  b = (dd2-dd1).days
  if b == 1:
    return '1 day'
  return '{} days'.format(b)

