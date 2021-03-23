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
  months={
  1:"January",
  2:"February",
  3:'March',
  4:'April',
  5:'May',
  6:"June",
  7:'July',
  8:'August',
  9:'September',
  10:'October',
  11:'November',
  12:'December'
  }
  if dateStart>dateEnd:
    [dateStart,dateEnd]=[dateEnd,dateStart]
  if dateStart.year==dateEnd.year:
    monthlist=list(range(dateStart.month,dateEnd.month+1))
  elif dateStart.year==dateEnd.year - 1:
    monthlist=list(range(dateStart.month,13))+list(range(1,dateEnd.month+1))
  else:
    monthlist=list(range(1,13))
  monthsnodupes=[]
  for month in monthlist:
    if month not in monthsnodupes:
      monthsnodupes.append(month)
  monthsnodupes.sort()
  output=[]
  for month in monthsnodupes:
    output.append(months[month])
  return(output)

