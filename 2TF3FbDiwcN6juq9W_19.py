"""


Given a `date`, return how many days `date` is away from 2021 (end date not
included). `date` will be in **mm/dd/yyyy** format.

### Examples

    days_until_2021("12/28/2020") ➞ "3 days"
    
    days_until_2021("1/1/2020") ➞ "366 days"
    
    days_until_2021("2/28/2020") ➞ "308 days"

### Notes

All given dates will be in the year 2020.

"""

def days_until_2021(date):
  class Date:
    def is_leapyear(year):
      if year %4 == 0:
        if year % 100 == 0:
          if year % 400 == 0:
            return True
          return False
        return True
      return False
      
    def __init__(self, date):
      self.date = date
      
      date = [int(i) for i in date.split('/')]
      
      self.month = date[0]
      self.day = date[1]
      self.year = date[2]
      
      self.ly = Date.is_leapyear(self.year)
    
    def days_till(self, other):
      months = {1: 31, 2: [28, 29], 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
      if self.year == other.year:
        selfdays = self.day
        for month in range(1, self.month):
          if month == 2:
            if self.ly == True:
              selfdays += months[month][1]
            else:
              selfdays += months[month][0]
          else:
            selfdays += months[month]
        
        otherdays = other.day
        for month in range(1, other.month):
          if month == 2:
            if other.ly == True:
              otherdays += months[month][1]
            else:
              otherdays += months[month][0]
          else:
            otherdays += months[month]
        
        if otherdays < selfdays:
          return False
        else:
          return otherdays - selfdays
      
      else:
        if self.year > other.year:
          return False
        
        selfdays = self.day
        for month in range(1, self.month):
          if month == 2:
            if self.ly == True:
              selfdays += months[month][1]
            else:
              selfdays += months[month][0]
          else:
            selfdays += months[month]
        
        if self.ly == True:
          diff = 366 - selfdays
        else:
          diff = 365 - selfdays
        
        for year in range(self.year + 1, other.year):
          if Date.is_leapyear(year) == True:
            diff += 366
          else:
            diff += 365
        
        for month in range(1, other.month):
          if month == 2:
            if other.ly == True:
              diff += months[month][1]
            else:
              diff += months[month][0]
          else:
            diff += months[month]
        
        diff += other.day
        
        return diff
  
  date1 = Date(date)
  date2 = Date('1/1/2021')
  
  days_till = date1.days_till(date2)
  
  if days_till == 1:
    return '1 day'
  else:
    return '{} days'.format(days_till)

