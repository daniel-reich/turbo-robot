"""


 **Mubashir** needs your help to find out next happy year.

A **Happy Year** is the year with only _distinct digits_. Create a function
that takes an integer `year` and returns the **next happy year**.

### Examples

    happy_year(2017) ➞ 2018
    # 2018 has all distinct digits
    
    happy_year(1990) ➞ 2013
    
    happy_year(2021) ➞ 2031

### Notes

N/A

"""

def happy_year(year):
  a = []
  while len(a)<4:
    year += 1
    a = set([i for i in str(year)])
  return year

