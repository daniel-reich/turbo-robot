"""


Given a range of years as a string, return the **number of leap years** there
are within the range (inclusive).

### Examples

    num_of_leapyears("1980-1984") ➞ 2
    # 1980 and 1984 are leapyears.
    
    num_of_leapyears("2000-2020") ➞ 6
    
    num_of_leapyears("1600-2000") ➞ 98

### Notes

  * Remember that a _hyphen_ separates the years.
  * Check the **Resources** tab for help on checking whether a year is a leap year.

"""

def num_of_leapyears(years):
    beg, end = years.split('-')
    return len([y for y in range(int(beg), int(end)+1) if is_leap(y)])
​
​
def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

