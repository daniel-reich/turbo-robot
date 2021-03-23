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

monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
def countLeapYears(d):
        years = int(d[2])
        if (int(d[1]) <= 2):
            years -= 1
        return int(years / 4) - int(years / 100) + int(years / 400)
def days_between_dates(dt1, dt2):
        dt1=(int(dt1[0:2]),int(dt1[2:4]),int(dt1[4:]))
        dt2=(int(dt2[0:2]),int(dt2[2:4]),int(dt2[4:]))   
        n1 = dt1[2] * 365 + dt1[0]   
        for i in range(0, dt1[1] - 1):
            n1 += monthDays[i]
        n1 += countLeapYears(dt1)
        n2 = dt2[2] * 365 + dt2[0]
        for i in range(0, dt2[1] - 1):
            n2 += monthDays[i]
        n2 += countLeapYears(dt2)
        return abs(n2 - n1)

