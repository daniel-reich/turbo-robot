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
    dates = []
    for i in lst:
        dates.append(datetime.strptime(i['date'], '%Y-%m-%d'))
        if i['date'] == today:
            break
        
    today = datetime.strptime(today, '%Y-%m-%d')
    dates = dates[::-1]
    count = 1
    a = [1]
    for i in range(len(dates)-1):
        if dates[i+1] == dates[i] - timedelta(days=1):
            count += 1
            a.append(count)
        else:
            break
        
    return 0 if not lst or today not in dates else max(a)

