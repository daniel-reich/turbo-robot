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
  small_bois = [4, 6, 9, 11]
  d, m, y = map(int, (date[:2], date[2:4], date[4:]))
  while days > 0:
    mdays = 30 if m in small_bois else 31
    
    if m == 2:
      mdays = 29 if is_leap(y) else 28
    
    if days >= mdays: 
      days -= mdays - d + 1
      m += 1
      d = 1
      if m > 12:
        m = 1
        y += 1
    else:
      d += days
      days = 0
      
  return '{:0>2}{:0>2}{:0>4}'.format(d,m,y) 
    
def is_leap(y):
  return y % 400 == 0 or y % 100 != 0 and y % 4 == 0

