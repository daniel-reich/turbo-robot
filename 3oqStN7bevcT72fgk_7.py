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

import datetime as dt
​
def get_day(day):
    """MM/DD/YYYY"""
    weekdays = {7:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    lst = [int(x) for x in day.split('/')]
    d = dt.date(lst[2], lst[0], lst[1]) # "YYYY,MM,DD"
    return weekdays[d.isoweekday()]

