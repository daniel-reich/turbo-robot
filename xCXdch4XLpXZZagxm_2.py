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
    lst = [int(i) for i in years.split('-')]
    leapyears = 0
    x = lst[1] - lst[0]
    first_year = lst[0]
    for i in range(x + 1):
        if first_year % 4 == 0:
            leapyears = leapyears + 1
            if first_year % 100 == 0 and first_year % 400 != 0:
                leapyears -= 1
        first_year += 1
    return leapyears

