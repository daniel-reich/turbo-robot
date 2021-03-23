"""


Every month, Microny™️ (a big entertainment corporation) publishes a few free
videogames on their web store. You are working on a script that will notify
you whenever the new games are available for download. There is not a fixed
date for the new releases, but you know that it happens every first Tuesday of
every month.

Write a function that, given a year and a month, returns a string with the
date of when the new games will be available.

### Examples

    first_tuesday_of_the_month(1997, 1) ➞ "1997-01-07"
    
    first_tuesday_of_the_month(2021, 2) ➞ "2021-02-02"
    
    first_tuesday_of_the_month(2020, 3) ➞ "2020-03-03"

### Notes

Months are given as numbers starting at 1 = January.

"""

from datetime import datetime
def first_tuesday_of_the_month(year, month, day=1):
  a = datetime(year, month, day).strftime("%A")
  b = {"Monday":2, "Tuesday":1, "Wednesday":7, "Thursday":6,
       "Friday":5, "Saturday":4, "Sunday":3}
  c = "0"+str(month) if month<10 else month
  return "{}-{}-0{}".format(year, c, b[a])

