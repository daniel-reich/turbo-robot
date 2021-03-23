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

from datetime import datetime, timedelta
​
​
def week_after(d):
    d = datetime.strptime(d, "%d/%m/%Y")
    week = timedelta(weeks=1)
    new_date = d + week
    return new_date.strftime("%d/%m/%Y")

