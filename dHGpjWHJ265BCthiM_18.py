"""


Create a function that takes the current day (e.g. `"2019-09-30"`), a list of
date dictionaries and returns the "current streak" (i.e. number of consecutive
days in a row).

### Examples

    current_streak("2019-09-23", [
      {
        "date": "2019-09-18"
      },
      {
        "date": "2019-09-19"
      },
      {
        "date": "2019-09-21"
      },
      {
        "date": "2019-09-22"
      },
      {
        "date": "2019-09-23"
      }
    ]) ➞ 3
    
    current_streak("2019-09-25", [
      {
        "date": "2019-09-16"
      },
      {
        "date": "2019-09-17"
      },
      {
        "date": "2019-09-21"
      },
      {
        "date": "2019-09-22"
      },
      {
        "date": "2019-09-23"
      }
    ]) ➞ 0

  * The list of dates is sorted chronologically.
  * The `today` parameter will always be greater than or equal to the last date in the list.
  * An empty list should return `0`.

"""

import datetime
def current_streak(today, lst):
  mem=[[]]
  for a,b in zip([day(i['date']) for i in lst],[day(i['date']) for i in lst][1:]):
    if b-a==datetime.timedelta(days=1):
      mem[-1]+=[a,b] if not a in mem[-1] else [b]
    else:mem[-1]+=[a] if not a in mem[-1] else [];mem+=[[b]]
  if len(lst)==1:mem[-1]+=[day(lst[-1]['date'])]
  mem= [i for i in mem if day(today) in i]+[[]]
  return len(mem[0])
  
def day(y_m_d):
  y,m,d=y_m_d.split('-')
  return datetime.date(int(y),int(m),int(d))

