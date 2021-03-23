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
  m=['January','February','March','April','May','June','July',
  'August','September','October','November','December']
  start=str(dateStart).split('-')
  end=str(dateEnd).split('-')
  if start[0]==end[0]:
    if start[1]==end[1]: return [m[int(start[1])-1]]
    else: 
      if int(start[1])>int(end[1]): start,end=end,start
      return m[int(start[1])-1:int(end[1])]
  elif abs(int(start[0])-int(end[0]))>1: return m
  else:
    if int(start[0])>int(end[0]): start,end=end,start
    ans=m[int(start[1])-1:]
    ans2=m[:int(end[1])]
    for i in ans2:
      if i not in ans: ans.append(i)
    return [i for i in m if i in ans]

