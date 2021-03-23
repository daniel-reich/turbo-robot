"""


Create a function `get_days` that takes two dates and returns the number of
days between the first and second date.

### Examples

    get_days(
      datetime.date(2019, 6, 14),  # June 14, 2019
      datetime.date(2019, 6, 20)  # June 20, 2019
    ) ➞ 6
    get_days(
      datetime.date(2018, 12, 29),  # December 29, 2018
      datetime.date(2019, 1, 1)  # January 1, 2019
    ) ➞ 3
    # Dates may not all be in the same month/year.
    get_days(
      datetime.date(2020, 5, 24),
      datetime.date(2019, 5, 24))
    ) ➞ -366
    # Backwards dates should return a negative change.

### Notes

N/A

"""

import datetime
​
def get_days(date1, date2):
  x = date2 - date1
  return x.days

