"""


Create a function that, given 2 dates, returns the names of the months that
are present between them (inclusive).

### Examples

**Input**

     january = datetime.date(2017, 1, 1)
     march = datetime.date(2017, 3, 1)
    
    monthsInterval(january, march)

**Output**

    ['January', 'February', 'March']

**Input**

     december = datetime.date(2017, 12, 1)
     january = datetime.date(2018, 1, 1)
    
    monthsInterval(december, january)

**Output**

    ['January', 'December']

**Input**

     january2017 = datetime.date(2017, 0, 1)
     january2018 = datetime.date(2018, 0, 1)
    
    monthsInterval(january2017, january2018)

**Output**

    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

(Notice that January is **not** duplicated!)

### Notes

  * The returned list should include the months of `dateStart` and `dateEnd` (inclusive)
  * The returned list **must not** include duplicate values
  * The month names returned by the function should be sorted (not alphabetically, but ordered by which comes first (January = 1st month, February = 2nd month, … , December = 12th month))
  * The function should produce the same output even if `dateStart` is greater than `dateEnd`

"""

def months_interval(dateStart, dateEnd):
  def get_month(date):
    return date.month
  def year_dif(date1, date2):
    y1 = date1.year
    y2 = date2.year
​
    if y1 == y2:
      return False
    else:
      m1 = date1.month
      m2 = date2.month
      print(m1, m2)
      months = 0
​
      if m1 > m2:
        months += (12 - m1)
        months += m2
      else:
        months = 12
    
      return months
  def month_namer(m1, m2):
​
    m1 -= 1
​
    months = 'January, February, March, April, May, June, July, August, September, October, November, December'.split(', ')
​
    month_range = range(m1, m2)
​
    tr = []
    for num in month_range:
      month = months[num]
      tr.append(month)
    
    return tr
​
  months = 'January, February, March, April, May, June, July, August, September, October, November, December'.split(', ')
​
  sm = get_month(dateStart)
  em = get_month(dateEnd)
​
  if sm > em and dateStart.year == dateEnd.year:
​
    de = dateStart
    ds = dateEnd
​
    dateStart = ds
    dateEnd = de
​
    del de
    del ds
​
    sm = get_month(dateStart)
    em = get_month(dateEnd)
  if dateStart.year > dateEnd.year:
​
    de = dateStart
    ds = dateEnd
​
    dateStart = ds
    dateEnd = de
​
    del de
    del ds
​
    sm = get_month(dateStart)
    em = get_month(dateEnd)
  
  yd = year_dif(dateStart, dateEnd)
  print(yd)
  if yd == False:
    mn = month_namer(sm, em)
  elif yd == 12:
    mn = months
  else:
    month_numbers = []
    for num in range(sm, sm + yd + 1):
      if num > 12:
        num -= 13
      elif num == 12:
        num -= 1
​
      month_numbers.append(num)
    
    mn = []
​
    for num in sorted(month_numbers):
      month = months[num]
      mn.append(month)
​
  
  return mn

