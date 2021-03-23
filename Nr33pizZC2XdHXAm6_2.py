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
  dates = [dateStart, dateEnd]
  dateStart, dateEnd = min(dates), max(dates)
​
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
​
  year_delta = dateEnd.year - dateStart.year
  month_delta = dateEnd.month - dateStart.month
  month_start_i = dateStart.month - 1
  month_end_i = dateEnd.month - 1
​
  if year_delta > 1 or (year_delta == 1 and month_delta >= 0):
    return months
  elif year_delta == 1 and month_delta < 0:
    return months[:month_end_i+1] + months[month_start_i:]
  else:
    return months[month_start_i : month_end_i+1]
