"""


Write a function that, given a date (in the format _MM/DD/YYYY_ ), returns the
day of the week as a string. Each day name must be one of the following
strings: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", or
"Saturday".

To illustrate, the day of the week for `"12/07/2016"` is `"Wednesday"`.

### Examples

    get_day("12/07/2016") ➞ "Wednesday"
    
    get_day("09/04/2016") ➞ "Sunday"
    
    get_day("12/08/2011") ➞ "Thursday"

### Notes

This challenge assumes the week starts on Sunday.

"""

import datetime
def get_day(day):
  date = day.split('/')
  m = int(date[0])
  d = int(date[1])
  y = int(date[2])
  return datetime.date(y,m,d).strftime("%A")

