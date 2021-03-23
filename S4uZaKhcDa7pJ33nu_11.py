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

from datetime import date, timedelta
​
​
def week_after(d):
  day, month, year = map(int, d.split('/'))
  week = date(year, month, day) + timedelta(days=7)
  return '{:02d}/{:02d}/{}'.format(week.day, week.month, week.year)
