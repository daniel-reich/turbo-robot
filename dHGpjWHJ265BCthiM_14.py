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
    y, m, d = [int(_) for _ in today.split('-')]
    baseline = datetime.datetime(y, m, d)
    if len(lst) == 0:
        return 0
    L = []
    for date in lst:
        y, m, d = [int(_) for _ in date["date"].split('-')]
        current = datetime.datetime(y, m, d)
        L.append((current - baseline).days)
    L.sort()
    if 0 not in L:
        return 0
    idx = L.index(0)
    ans = 1
    k = 1
    while idx + k < len(L) and L[idx + k] == k:
        ans += 1
        k += 1
    k = 1
    while idx - k >= 0 and L[idx - k] == -k:
        ans += 1
        k += 1
    return ans

