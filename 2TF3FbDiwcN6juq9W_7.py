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
  a, b, c = date.split("/")
  d = datetime.datetime(int(c), int(a), int(b)).timestamp()
  e = datetime.datetime(2021, 1, 1).timestamp()
  f = int((e - d)//86400)
  return '{} day{}'.format(f ,"s" if f>1 else "")

