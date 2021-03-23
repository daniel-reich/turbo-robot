"""


Create a function that takes the current day (e.g. `"2019-09-30"`), a list of
date dictionaries and returns the "current streak" (i.e. number of consecutive
days in a row).

### Examples

    current_streak("2019-09-23", [
      {
        "date": "2019-09-18"
      },
      {
        "date": "2019-09-19"
      },
      {
        "date": "2019-09-21"
      },
      {
        "date": "2019-09-22"
      },
      {
        "date": "2019-09-23"
      }
    ]) ➞ 3
    
    current_streak("2019-09-25", [
      {
        "date": "2019-09-16"
      },
      {
        "date": "2019-09-17"
      },
      {
        "date": "2019-09-21"
      },
      {
        "date": "2019-09-22"
      },
      {
        "date": "2019-09-23"
      }
    ]) ➞ 0

  * The list of dates is sorted chronologically.
  * The `today` parameter will always be greater than or equal to the last date in the list.
  * An empty list should return `0`.

"""

def current_streak(today, lst):
  def ly_dic_or_not(year):
    ly = {'1': 31, '2': 29, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    nly = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    
    if year%4 == 0:
      if year%100 == 0:
        if year%400 == 0:
          return ly
        else:
          return nly
      return ly
    return nly
  def day_count(lst, today, dic):
    years = []
    months = []
    days = []
    for date in lst:
      date = date.split('-')
      year = int(date[0])
      month = date[1]
      day = int(date[2])
      years.append(year)
      months.append(month)
      days.append(day)
    minim = min(years)
    year = 365
    tr = []
    for n in range(0, len(years)):
      year = years[n]
      month = months[n]
      day = days[n]
      dc = 0
      while year > minim:
        dc += year
        year -= 1
      for n in range(1, int(month)):
        dc += dic[str(n)]
      dc += day
      tr.append(dc)
    
    ty = int(today[0])
    tm = today[1]
    td = int(today[2])
    
    tdc = 0
    
    while ty > minim:
      tdc += year
      ty -= 1
    
    for n in range(1, int(tm)):
      tdc += dic[str(n)]
    
    tdc += td
    return [tr, tdc]
  
  if lst == []:
    return 0
  dates = []
  
  t = today.split('-')
  ty = int(t[0])
  tm = t[1]
  td = int(t[2])
  
  dic = ly_dic_or_not(ty)
  
  for date in lst:
    dates.append(date['date'])
    
  d = day_count(dates, t, dic)
  
  lst_days = d[0]
  today_days = d[1]
  
  current = 0
  
  if today_days in lst_days:
    current += 1
  
  today_days -= 1
  
  while today_days in lst_days:
    current += 1
    today_days -= 1
  
  return current

