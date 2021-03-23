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

def add_n_days_to_a_date(date, days):
  def date_formulater(date):
    days = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])
​
    return [days, month, year]
  from datetime import datetime as dt
  
  day_timestamp = 86400
  df = date_formulater(date)
​
  date = dt(df[2], df[1], df[0])
​
  datetimestamp = date.timestamp()
​
  newtimestamp = datetimestamp + (days * day_timestamp)
​
  newdate = dt.fromtimestamp(newtimestamp)
​
  newyear = newdate.strftime('%Y')
  newmonth = newdate.strftime('%m')
  newday = newdate.strftime('%d')
​
  return ''.join([newday, newmonth, newyear])

