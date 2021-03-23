"""


In this challenge, sort a list containing a series of dates given as strings.
Each date is given in the format `DD-MM-YYYY_HH:MM`:

    "12-02-2012_13:44"

The priority of criteria used for sorting will be:

  * Year
  * Month
  * Day
  * Hours
  * Minutes

Given a list `lst` and a string `mode`, implement a function that returns:

  * if `mode` is equal to `"ASC"`, the list `lst` sorted in ascending order.
  * if `mode` is equal to `"DSC"`, the list `lst` sorted in descending order.

### Examples

    sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC") ➞ ["10-02-2016_12:30", "10-02-2018_12:15", "10-02-2018_12:30"]
    
    sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC") ➞ ["10-02-2018_12:30", "10-02-2018_12:15", "10-02-2016_12:30"]
    
    sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC") ➞ ["01-01-1999_00:55", "09-02-2000_10:03", "10-02-2000_18:29"]

### Notes

  * Remember: the date is in the format `DD-MM-YYYY_HH:MM`.
  * You can expect only valid formatted dates, without exceptions to handle.

"""

import datetime as d
def sort_dates(lst, mode):
  result = []
  result1 = []
  for i in lst:
    year = int(i[6:10])
    month = int(i[3:5])
    date = int(i[:2])
    hour = int(i[11:13])
    min = int(i[14:])
    sec = 0
    milsec = 0
    result.append(d.datetime(year, month, date, hour, min, sec, milsec))
  if mode == 'ASC':
    result.sort()
  else:
    result.sort(reverse=True)
  for j in result:
    d1 = str(j.day) if len(str(j.day))>1 else '0'+str(j.day)
    m1 = str(j.month) if len(str(j.month))>1 else '0'+str(j.month)
    y1 = str(j.year)
    h1 = str(j.hour) if len(str(j.hour))>1 else '0'+str(j.hour)
    mi1 = str(j.minute) if len(str(j.minute))>1 else '0'+str(j.minute)
    result1.append(d1+'-'+m1+'-'+y1+"_"+h1+':'+mi1)
  return result1

