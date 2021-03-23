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

dpm = [31,28,31,30,31,30,31,31,30,31,30,31]
def leap_year(y):
  if y % 4 == 0:
    if y % 100 == 0:
      return y % 400 == 0
    return True
  return False
dpy = lambda x: 366 if leap_year(x) else 365
string = lambda x: '0' + str(x) if x < 10 else str(x)
class Date:
  def __init__(self,date):
    self.y = int(date[4::])
    self.m = int(date[2:4])
    self.d = int(date[:2])
  def nth_day(self):
    if self.d == 29 and self.m == 2:
      return 60
    days = sum(dpm[:self.m-1]) + self.d
    if leap_year(self.y) and self.m > 2:
      days += 1
    return days
  def increment_year(self):
    self.y += 1
  def until_jan(self):
    return dpy(self.y) - self.nth_day()
  def get_date(self,n):
    if n < 31:
      return str(n+1) + '01' + str(self.y)
    n -= 31
    if n < 28:
      return str(n+1) + '02' + str(self.y)
    n-=28
    if leap_year(self.y):
      if n == 1:
        return "2902" + str(self.y)
      else:
        n -= 1
    for i in range(2,12):
      if n < dpm[i]:
        return string(n) + string(i+1) + str(self.y)
      n -= dpm[i]
​
def add_n_days_to_a_date(date, days):
  date = Date(date)
  if days < date.until_jan():
    return date.get_date(date.nth_day()+days)
  days -= date.until_jan()
  date = Date('0101' + str(date.y+1))
  while days > dpy(date.y):
    days -= dpy(date.y)
    date.increment_year()
  return date.get_date(days)

