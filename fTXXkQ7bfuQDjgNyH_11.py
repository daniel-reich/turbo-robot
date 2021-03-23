"""


Each year has 365 or 366 days. Given a string `date` representing a Gregorian
calendar date formatted as `month/day/year`, return the _day-number_ of the
year.

### Examples

    day_of_year("11/16/2020") ➞ 321
    
    day_of_year("1/9/2019") ➞ 9
    
    day_of_year("3/1/2004") ➞ 61
    
    day_of_year("12/31/2000") ➞ 366

### Notes

All input strings in tests are valid dates.

"""

class Date:
  
  def is_leapyear(year):
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          return True
        return False
      return True
    return False
  
  thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
  
  def __init__(self, date):
    
    self.date = date
    
    d = [int(dte) for dte in date.split('/')]
    self.month = d[0]
    self.day = d[1]
    self.year = d[2]
    self.ly = Date.is_leapyear(self.year)
    
    self.days_in_year = self.day
    
    for n in range(1, self.month):
      if n == 2:
        if self.ly == True:
          self.days_in_year += 29
        else:
          self.days_in_year += 28
      elif n in Date.thirty_one_days:
        self.days_in_year += 31
      else: 
        self.days_in_year += 30
​
def day_of_year(date):
  
  date = Date(date)
  
  return date.days_in_year

