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
  x = years.split("-")
  def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
  count  = 0
  for year in range(int(x[0]),int(x[1])+1):
    if is_leap_year(year):
      count+= 1
  return count

