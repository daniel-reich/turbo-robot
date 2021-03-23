"""


Each year has 365 or 366 days. Given a string `date` representing a Gregorian
calendar date formatted as `month/day/year`, return the _day-number_ of the
year.

### Examples

    day_of_year("11/16/2020") ➞ 321
    
    day_of_year("1/9/2019") ➞ 9
    
    day_of_year("3/1/2004") ➞ 61
    
    day_of_year("12/31/2000") ➞ 366

### Notes

All input strings in tests are valid dates.

"""

def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        return 29 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 28
    return 31
​
def day_of_year(date):
    month, day, year = [int(_) for _ in date.split('/')]
    if month == 1:
        return day
    return sum([days_in_month(m, year) for m in range(1, month)]) + day

