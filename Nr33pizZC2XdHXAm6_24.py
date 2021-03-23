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
  if dateStart - dateEnd > datetime.timedelta(0):
    a1 = dateEnd
    a2 = dateStart
  else:
    a1 = dateStart
    a2 = dateEnd
  m =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  i = a1.month
  lst = {i-1:m[i-1]}
  while a1.month != a2.month or a1.year != a2.year:
    i += 1
    if i > 12:
      i = i - 12
      a1 = datetime.date(a1.year +1 , i , 1)
    a1 = datetime.date(a1.year , i , 1)
    if not m[i-1] in lst:
      lst.update({i-1:m[i-1]})
  return [lst[i] for i in sorted(lst.keys())]

