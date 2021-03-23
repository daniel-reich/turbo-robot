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
def current_streak(today, lst):
  if len(lst) == 0 or lst[-1]['date'] != today:
    return 0
  lst=lst[::-1]
  streak = 1
  for i, j in zip(lst, lst[1:]):
    t1 = datetime.strptime(i['date'],'%Y-%m-%d')
    t2 = datetime.strptime(j['date'],'%Y-%m-%d')
    if t1-t2 == timedelta(1):
      streak += 1
    else:
      return streak
  return streak

