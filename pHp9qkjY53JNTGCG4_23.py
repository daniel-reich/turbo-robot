"""


Write a function that takes a `year` and returns its corresponding century.

### Examples

    century_from_year(2005) ➞ 21
    
    century_from_year(1950) ➞ 20
    
    century_from_year(1900) ➞ 19

### Notes

For guidance on the year boundaries for each century:

  * The 19th century are the years from 1801 to 1900.
  * The 20th century are the years from 1901 to 2000.

"""

def century_from_year(n):
    if n % 100 == 0:
        return n // 100
    else:
        return n // 100 + 1
