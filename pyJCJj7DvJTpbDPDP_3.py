"""


Your task is to calculate the number of **days** between two dates. The dates
will be in the format **DDMMYYYY**. You are **not** allowed to import any
modules, especially the datetime module. The days will not include the end
date in calculation.

Remember to consider all leap years and leap months. The order of the larger
date and smaller date don't matter, as the days between them are the same
anyways.

### Examples

    days_between_dates("01012020", "02012020") ➞ 1
    
    days_between_dates("03101999", "02023000") ➞ 365,365
    
    days_between_dates("03101534", "07013443") ➞ 696,969
    
    days_between_dates("30012020", "01012020") ➞ 29

### Notes

  * Take note that a leap year is divisible by 4. However, if it is a new century (like 1900, 2400, etc), check its divisibility by 400. If it doesn't divvy into a whole number, then it is not a leap year (1900 isn't a leap year but 2400 is).
  * Do comment if there are any bugs or problems.

"""

class Date:
  thirty_one = [1, 3, 5, 7, 8, 10, 12]
  def is_leapyear(year):
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          return True
        return False
      return True
    return False
    
  def __init__(self, string):
    
    self.raw = string
    
    self.day = int(string[:2])
    self.month = int(string[2:4])
    self.year = int(string[4:])
    
    self.days_since_start = 0
    
    for year in range(1, self.year):
      if Date.is_leapyear(year) == True:
        self.days_since_start += 366
      else:
        self.days_since_start += 365
    
    for month in range(1, self.month):
      if month in Date.thirty_one:
        self.days_since_start += 31
      elif month == 2:
        if Date.is_leapyear((self.year)) == True:
          self.days_since_start += 29
        else:
          self.days_since_start += 28
      else:
        self.days_since_start += 30
    
    self.days_since_start += self.day
  
  def days_between(self, other):
    return abs(self.days_since_start - other.days_since_start)
​
def days_between_dates(d1, d2):
​
  d1 = Date(d1)
  d2 = Date(d2)
  
  return d1.days_between(d2)

