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

def num_of_leapyears(string):
    counter = 0
    string = string.split("-")
    for i in range(int(string[0]), int(string[1]) + 1):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            counter += 1
    return counter

