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

from datetime import datetime, timedelta
​
def current_streak(today, lst):
    x = 0
    lst3 = lst[::-1]
    if len(lst) == 0:
        return 0
    elif datetime.strptime(lst3[0]["date"], '%Y-%m-%d').date() == datetime.strptime(today, '%Y-%m-%d').date():
        for i, e in enumerate(lst3):
            if datetime.strptime(e["date"], '%Y-%m-%d').date() == datetime.strptime(today, '%Y-%m-%d').date():
                x = x+1
            elif datetime.strptime(e["date"], '%Y-%m-%d').date() == datetime.strptime(today, '%Y-%m-%d').date() - timedelta(days=i):
                x = x + 1
        return x
    else:
        return 0

