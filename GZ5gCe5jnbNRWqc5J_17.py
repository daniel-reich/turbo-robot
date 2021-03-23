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

def first_tuesday_of_the_month(year, month): 
  from datetime import date as d
  day = 1
  while d(year, month, day).weekday() != 1:
    day += 1
  
  year, month, day = [str(item) for item in [year, month, day]]
  
  while len(month) < 2:
    month = '0' + month
  while len(day) < 2:
    day = '0' + day
  
  return '-'.join([year, month, day])

