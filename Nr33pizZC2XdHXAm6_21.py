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
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  m1 = dateStart.strftime("%B")
  m2 = dateEnd.strftime('%B')
  y1 = int(dateStart.strftime("%Y"))
  y2 = int(dateEnd.strftime('%Y'))
  i1 = months.index(m1)
  i2 = months.index(m2)
  if y1 == y2:
    if i1 > i2:
      return months[i2:i1+1]
    elif i1 == i2:
      return [months[i1]]
    else:
      return months[i1:i2+1]
  elif y1 < y2:
    chonk1 = months[i1:]
    chonk2 = months[:i2+1]
    l = chonk1 + chonk2
  else:
    chonk1 = months[i2:]
    chonk2 = months[:i1+1]
  for el in chonk1:
    if el in chonk2:
      chonk2.remove(el)
  l = chonk1 + chonk2
  l1 = []
  for m in months:
    if m in l:
      l1.append(m)
  return l1

