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

from datetime import timedelta
import datetime
def week_after(d):
  date = d.split("/")
  year = int(date[2])
  month = int(date[1])
  day = int(date[0])
  x = datetime.datetime(year, month, day)
  one_week = x + timedelta(days = 7)
  return one_week.strftime("%d"+"/""%m"+"/""%Y")

