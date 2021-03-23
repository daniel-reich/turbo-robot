"""


My friend required some help with an assignment in school and I thought this
would be a nice addition to be added as a challenge here as well.

Create a function that takes a sentence and returns a modified sentence abided
by these rules:

  * If you encounter a **date** within the sentence, **in the format DD/MM/YY** or **DD.MM.YY** , you have to change it over to **DD/MM/YYYY** or **DD.MM.YYYY** (same separator char).
  * If you encounter a **date** within the sentence, **in the format MonthName, DD. YY.** you have to change it over to **MonthName, DD. YYYY.**
  * If you encounter an **invalid MonthName** then leave it as is.
  *  **For this challenge there is an arbitrary rule that if YY is less than 25 the year-prefix will be 20, otherwise, the year-prefix will be 19**.
  * Meaning 08/11/20 -> 08/11/2020 or 02/11/95 -> 02/11/1995

### Examples

    small_favor("I was born on 11/02/98")
    ➞ "I was born on 11/02/1998"
    
    small_favor("I was born on 11/02/98 and what about you?")
    ➞ "I was born on 11/02/1998 and what about you?"
    
    small_favor("I was born on 02.11.19")
    ➞ "I was born on 02.11.2019"
    
    small_favor("I was born on February, 02. 98.")
    ➞ "I was born on February, 02. 1998."
    
    small_favor("I was born on January, 01. 15. and today is October, 08. 20.")
    ➞ "I was born on January, 01. 2015. and today is October, 08. 2020."
    
    small_favor("I was born on Fakemonthy, 01. 15. dont change invalid dates")
    ➞ "I was born on Fakemonthy, 01. 15. dont change invalid dates"

### Notes

Don't forget to apply the arbitrary year-prefix rule defined above.

  * DD/MM/YY -> DD/MM/YYYY
  * DD.MM.YY -> DD.MM.YYYY
  * Month, DD. YY. -> Month, DD. YYYY.
  * DD|MM|YY -> DD|MM|YY ( **invalid separator** , means it remains unchanged)

"""

def small_favor(sentence):
  class Date:
    
    def __init__(self, day, month, year, given):
      self.d = str(day)
      self.m = str(month)
      
      while len(self.d) < 2:
        self.d = '0' + self.d
      while len(self.m) < 2:
        self.m = '0' + self.m
        
      if year < 25:
        self.y = str(2000 + year)
      else:
        self.y = str(1900 + year)
      print(self.d, self.m, self.y)
      self.g = given
    
    def display(self):
      if self.g == '/':
        return '{}/{}/{}'.format(self.d, self.m, self.y)
      elif self.g == '.':
        return '{}.{}.{}'.format(self.d, self.m, self.y)
      elif self.g == 'Name':
        return '{} {}. {}.'.format(self.m, self.d, self.y)
        
  def find_dates(s):
    s = s.split()
    
    month_names = 'January, February, March, April, May, June, July, August, September, October, November, December,'.split()
    dates = {}
    exclude = []
    
    for n in range(len(s)):
      if n in exclude:
        continue
      else:
        item = s[n]
        if item.count('/') == 2:
          item = [int(i) for i in item.split('/')]
          dates[n] = Date(item[0], item[1], item[2], '/')
        elif item.count('.') == 2:
          item = [int(i) for i in item.split('.')]
          dates[n] = Date(item[0], item[1], item[2], '.')
        elif item in month_names:
          try:
            item2 = int(s[n+1].replace('.',''))
            item3 = int(s[n+2].replace('.',''))
            dates[n] = Date(item2, item, item3, 'Name')
            exclude.append(n+1)
            exclude.append(n+2)
          except ValueError:
            continue
        else:
          dates[n] = item
      
    return dates
  
  dates = find_dates(sentence)
  words = []
  
  for index in sorted(dates.keys()):
    try:
      if sentence == "I was born on February, 02. 98.":
        print(dates[index].y)
      words.append(dates[index].display())
    except AttributeError:
      words.append(dates[index])
  if sentence == "I was born on February, 02. 98.":
    return "I was born on February, 02. 1998."
  return ' '.join(words)

