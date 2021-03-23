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
  def is_leap(year):
    if year % 4 != 0:
      return False
    elif year % 100 != 0:
      return True
    elif year % 400 != 0:
      return False
    return True
  start, end = [int(num) for num in years.split('-')]
  counter = 0
  cur_year = start
  while not is_leap(cur_year):
    cur_year += 1
  for year in range(cur_year, end + 1, 4):
    if is_leap(year):
      counter += 1
  return counter

