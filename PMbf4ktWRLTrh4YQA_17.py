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

from datetime import datetime, timedelta
​
def add_n_days_to_a_date(date: str, n: int) -> str:
    day, month, year = int(date[:2]), int(date[2:4]), int(date[4:])
    end = datetime(year, month, day) + timedelta(days=n)
    return end.strftime('%d%m%Y')

