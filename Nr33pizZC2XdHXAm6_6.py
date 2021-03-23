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

from dateutil.relativedelta import *
def months_interval(dateStart, dateEnd):
  months = {'January':0,'February':1,'March':2,'April':3,'May':4,'June':5,'July':6,'August':7, 'September':8,'October':9,'November':10,'December':11}
  def month_range(date1,date2):
    z = []
    while((date1!=date2)):#| (len(z)<12)
      z = z +[date1.strftime('%B')]
      date1 = date1+ relativedelta(months=+1)
​
    return z + [date2.strftime('%B')]
​
  if(dateStart>dateEnd):
    return sorted(list(set(month_range(dateEnd,dateStart))), key=months.get)
  elif(dateStart==dateEnd):
    return [dateStart.strftime('%B')]
  elif(dateStart<dateEnd):
    return sorted(list(set(month_range(dateStart,dateEnd))), key=months.get)

