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
  years_list = years.split('-')
  def leap_year(year):
    if not year % 400:
      return True
    if not year % 100:
      return False
    if not year % 4:
      return True
    else:
      return False
  return sum([leap_year(int(i)) for i in range(int(years_list[0]), int(years_list[1]) + 1)])

