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
​
def date_conversion(inp):
    return datetime(int(inp[0:4]), int(inp[5:7]), int(inp[8:]))
​
def current_streak(today, lst):
    if lst and lst[-1]['date'] == today:
        res = 1
        for d in range(len(lst) - 1, 0, -1):
            if date_conversion(lst[d]['date']) - date_conversion(lst[d-1]['date']) == timedelta(days=1):
                res+=1
            else:
                break
    else:
        return 0
    return res

