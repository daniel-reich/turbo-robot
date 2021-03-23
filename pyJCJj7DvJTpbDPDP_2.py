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

def leap_year(y):
    return y%400 == 0 or (y%4 == 0 and y%100 != 0)
​
def days_between_dates(date1, date2):
    date1, date2 = sorted((date1, date2), key=lambda x: int(x[-4:] + x[2:4] + x[:2]))
    d1, m1, y1 = int(date1[:2]), int(date1[2:4]), int(date1[-4:])
    d2, m2, y2 = int(date2[:2]), int(date2[2:4]), int(date2[-4:])
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    months[1] = 29 if leap_year(y2) else 28
    partial_1 = d2 if m2 == 1 else sum(months[:m2-1]) + d2
    months[1] = 29 if leap_year(y1) else 28
    partial_2 = sum(months[m1-1:]) - d1
    year_days = sum(366 if leap_year(y) else 365 for y in range(y1+1, y2))
    total = partial_1 + partial_2 + year_days
    
    if y1 == y2:
        return total - 366 if leap_year(y1) else total - 365
    return total

