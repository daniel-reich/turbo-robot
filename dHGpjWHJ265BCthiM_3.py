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

"""this script is used to count number of consecutive day in a list"""
from datetime import datetime, timedelta
def current_streak(today, lst):
    """this is the main function used to return number of consecutuve day in list"""
    nb_day = 0
    new_list = [val['date'] for val in lst]
    if today not in new_list:
        return nb_day
    delta = timedelta(days=1)
    today = datetime.strptime(today, '%Y-%m-%d')
    for element in reversed(new_list):
        consecutive_date = datetime.strptime(element, '%Y-%m-%d')
        if today != consecutive_date:
            return nb_day
        nb_day += 1
        today -= delta
    return nb_day

