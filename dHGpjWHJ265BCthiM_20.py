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
def make_date(date):
    year, month, day = map(int, date.split('-'))
    return datetime(year=year, month=month, day=day)
​
​
def current_streak(today, lst):
    if not lst or today != lst[-1]['date']:
        return 0
    dates = [make_date(i['date']) for i in lst[::-1]]
    delta = timedelta(days=-1)
    streak = 1
    for i, j in zip(dates, dates[1:]):
        if i + delta != j:
            break
        else:
            streak += 1
    return streak

