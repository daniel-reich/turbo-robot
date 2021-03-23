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

import datetime
def months_interval(dateStart, dateEnd):
    dateStart,dateEnd = min(dateStart,dateEnd),max(dateStart,dateEnd)
    
    month_list = []
    d = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    
    year_diff = dateEnd.year - dateStart.year
    month_diff = dateEnd.month - dateStart.month
    
    total_month_diff = (year_diff*12)+month_diff
    
    if total_month_diff > 11:
        month_list = list(d.values())
    else:
        for month in range(dateStart.month,dateStart.month+total_month_diff+1):
            mcopy = month
            if mcopy > 12:
                mcopy -= 12
            month_list.append(d[mcopy])
            
    return [i for i in list(d.values()) if i in month_list]

