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
  if lst == []: return 0
  if today != lst[-1]["date"]: return 0
  con = 1
  lst.reverse()
  for i in range(len(lst)- 1):
    if int(lst[i]["date"][-2:]) -1 == int(lst[i+1]["date"][-2:]):
      con += 1
    else:
      break
  return con

