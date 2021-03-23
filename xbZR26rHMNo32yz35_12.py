"""


Create a function that takes the age and return the age in days.

### Examples

    calc_age(65) ➞ 23725
    
    calc_age(0) ➞ 0
    
    calc_age(20) ➞ 7300

### Notes

  * Use **365 days** as the length of a year for this challenge.
  * Ignore leap years and days between last birthday and now.
  * Expect only positive integer inputs.

"""

def calc_age(age):
  year_age = age
  age_in_days = year_age * 365
  return age_in_days

