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
​
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
​
def months_interval(dateStart, dateEnd):
    year1 = dateStart.year
    month1 = dateStart.month - 1
    year2 = dateEnd.year
    month2 = dateEnd.month - 1
    if (year1, month1) > (year2, month2):
        year1, month1, year2, month2 = year2, month2, year1, month1
    if year2 - year1 > 1:
        return MONTHS
    if year1 == year2 and month1 == month2:
        return [MONTHS[month1]]
    if year2 == year1:
        return MONTHS[month1:month2+1]
    if year2 == year1 + 1:
        months = set()
        months.add(MONTHS[month1])
        while (year1 != year2) or (month1 != month2):
            month1 += 1
            if month1 == 12:
                year1 += 1
                month1 = 0
            months.add(MONTHS[month1])
        months = [[m, MONTHS.index(m)] for m in months]
        months.sort(key=lambda x: x[1])
        return [m[0] for m in months]

