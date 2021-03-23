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

from datetime import datetime
​
def days_until_2021(date):
  a = datetime.strptime(date, "%m/%d/%Y")
  b = datetime.strptime('1/1/2021', "%m/%d/%Y")
  return "{} day{}".format((b-a).days, 's' if (b-a).days>1 else '')

