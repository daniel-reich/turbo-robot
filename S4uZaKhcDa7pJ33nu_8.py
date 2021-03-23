"""


Create a function which takes in a date as a string, and **returns the date a
week after**.

### Examples

    week_after("12/03/2020") ➞ "19/03/2020"
    
    week_after("21/12/1989") ➞ "28/12/1989"
    
    week_after("01/01/2000") ➞ "08/01/2000"

### Notes

  * Note that dates will be given in **day/month/year** format.
  * Single digit numbers should be **zero padded**.
  * See **Resources** for some helpful tutorials on Python dates.

"""

import datetime
​
def week_after(d):
    day, month, year = list(map(int ,d.split('/')))
    date = datetime.date(year, month, day)
    delta = datetime.timedelta(days=7)
    return "{2}/{1}/{0}".format(*(str(date + delta).split('-')))

