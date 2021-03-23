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

month_days = [[0,31,59,90,120,151,181,212,243,273,304,334,365],
        [0,31,60,91,121,152,182,213,244,274,305,335,366]]
is_leap = lambda y: (y%100 and y%4 == 0) or y%400 == 0
​
def add_n_days_to_a_date(date, days):
  d, m, y = int(date[:2]), int(date[2:4]), int(date[4:]),
  ly = is_leap(y)
  doy = d + month_days[ly][m-1]
  remDays = [365, 366][ly] - doy
  if days <= remDays:
    yr, doyr = y, doy + days
  else:
    days -= remDays
    yr = y + 1
    ly = is_leap(yr)
    yr_days = [365, 366][ly]
    while days >= yr_days:
      days -= yr_days
      yr += 1
      ly = is_leap(yr)
      yr_days = [365, 366][ly]
    doyr = days
  for i in range(1, 13):
    if doyr <= month_days[ly][i]:
      mr = i
      dr = doyr - month_days[ly][i-1]
      break
​
  return '{:0>2}{:0>2}{}'.format(str(dr), str(mr), str(yr))

