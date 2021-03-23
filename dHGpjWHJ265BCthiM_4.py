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

monthlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def process_date(date):
  return (int(date[0:4]), int(date[5:7]), int(date[8:10]))
def is_next(last, year, month, day): 
   if last[0] == 0:
     return True
   elif (year == last[0] and month == last[1] and day == last[2]+1):
     return True
   elif (year == last[0] and month == last[1] + 1 and day == 1 and last[2] >= monthlength[last[1]-1]):
       return True
   elif (year == last[0] + 1 and month == 1 and day == 1 and  last[1] == 12 and last[2] == 31):
     return True
   else:
     return False 
def current_streak(today, lst):
  if(len(lst) == 0):
      return 0
  last = (0, 0, 0)
  streak = 0
  for entry in lst:
    string = entry['date']
    year, month, day = (process_date(string))
    if (is_next(last, year, month, day)):
      streak += 1
      print(streak)
    else:
      streak = 1;
    last = (year, month, day)
  year, month, day = (process_date(today))
  if (is_next(last, year, month, day)):
      return (streak + 1)
  elif (year, month, day) == last: 
      return streak
  else:
      return 0

