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

from datetime import datetime as dt
def days_until_2021(date):
  diff = dt(2021,1,1) - dt.strptime(date,'%m/%d/%Y')
  return '{} days'.format(diff.days) if diff.days != 1 else '1 day'

