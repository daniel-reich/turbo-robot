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
​
def current_streak(today, lst):
    if len(lst) == 0:
        return 0
    t = datetime.datetime.strptime(today, '%Y-%m-%d')
    t = int(t.strftime('%j'))
​
    d = []
    for i in range(len(lst)):
        x = lst[i]['date']
        temp = datetime.datetime.strptime(x, '%Y-%m-%d')
        d.append(int(temp.strftime('%j')))
​
    if d[-1] != t:
        return 0
​
    for i in range(len(d)-1,-1,-1):
        if d[i] - d[i-1] != 1:
            return t-d[i]+1

