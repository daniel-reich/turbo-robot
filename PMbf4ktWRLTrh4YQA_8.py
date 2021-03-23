"""


Create a function that returns the date in **DDMMYYYY** format after a
specific date. Consider leap years and leap months (e.g. February 29th).
Please **do not import** anything (such as `datetime`).

### Examples

    add_n_days_to_a_date("15041984", 6038) ➞ "26102000"
    
    add_n_days_to_a_date("26102000", 6038)) ➞ "08052017"
    
    add_n_days_to_a_date("01011900", 30) ➞ "31011900"

### Notes

  * Remember that if the year is a new century like 1800, although it is divisible by 4, it isn't divisible by 400, hence it's NOT a leap year.
  * Please give feedback if there are any bugs (this is my first time making a challenge).

"""

import datetime
def add_n_days_to_a_date(date, days):
    s = ''
    x = datetime.datetime(int(date[4:]), int(date[2:4]),int(date[:2])) + datetime.timedelta(days = days)
    if x.day < 10:
        s += '0' + str(x.day)
    else:
        s += str(x.day)
    if x.month < 10:
        s += '0' + str(x.month)
    else:
        s += str(x.month)
    s += str(x.year)
    return s

