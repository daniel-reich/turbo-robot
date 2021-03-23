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

def current_streak(today, lst):
  if len(lst) == 0: return 0
  if lst[-1].get('date') != today: return 0
  max = 0
  cnt = 0
  prev = 'none'
  for i in lst:
    if prev == 'none': 
      prev = i.get('date')[-2:]
      cnt = 1
    elif int(i.get('date')[-2:])-1 == int(prev):
      cnt += 1
      prev = i.get('date')[-2:]
    else:
      if cnt > max and prev == lst[-1].get('date'): max = cnt
      prev = i.get('date')[-2:]
      cnt = 1
  if cnt > max: max = cnt
  return max

