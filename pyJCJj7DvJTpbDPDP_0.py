"""


Your task is to calculate the number of **days** between two dates. The dates
will be in the format **DDMMYYYY**. You are **not** allowed to import any
modules, especially the datetime module. The days will not include the end
date in calculation.

Remember to consider all leap years and leap months. The order of the larger
date and smaller date don't matter, as the days between them are the same
anyways.

### Examples

    days_between_dates("01012020", "02012020") ➞ 1
    
    days_between_dates("03101999", "02023000") ➞ 365,365
    
    days_between_dates("03101534", "07013443") ➞ 696,969
    
    days_between_dates("30012020", "01012020") ➞ 29

### Notes

  * Take note that a leap year is divisible by 4. However, if it is a new century (like 1900, 2400, etc), check its divisibility by 400. If it doesn't divvy into a whole number, then it is not a leap year (1900 isn't a leap year but 2400 is).
  * Do comment if there are any bugs or problems.

"""

days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                 9: 30, 10: 31, 11: 30, 12: 31}
​
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
​
def days_between_dates(d1, d2):
    day1 = int(d1[:2])
    month1 = int(d1[2:4])
    year1 = int(d1[4:])
    day2 = int(d2[:2])
    month2 = int(d2[2:4])
    year2 = int(d2[4:])
    if year1 > year2 or (year1 == year2 and month1 > month2) or \
       (year1 == year2 and month1 == month2 and day1 > day2):
        day1, month1, year1, day2, month2, year2 = day2, month2, year2, day1, month1, year1
    diff = 0
    while (day1, month1, year1) != (day2, month2, year2):
        diff += 1
        day1 += 1
        d = days_in_month[month1]
        if month1 == 2 and is_leap_year(year1):
            d += 1
        if day1 > d:
            day1 = 1
            month1 += 1
            if month1 == 13:
                month1 = 1
                year1 += 1
    return diff

