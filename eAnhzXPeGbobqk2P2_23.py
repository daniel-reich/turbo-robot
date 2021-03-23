"""


Create a function that takes in a year and returns the correct century.

### Examples

    century(1756) ➞ "18th century"
    
    century(1555) ➞ "16th century"
    
    century(1000) ➞ "10th century"
    
    century(1001) ➞ "11th century"
    
    century(2005) ➞ "21st century"

### Notes

  * All years will be between `1000` and `2010`.
  * The 11th century is between 1001 and 1100.
  * The 18th century is between 1701-1800.

"""

from math import ceil
def century(year):
  suffix = 'th'
  if str(ceil(year / 100))[-1] == '1' and str(ceil(year / 100))[-2] != '1':
    suffix = 'st'
  elif str(ceil(year / 100))[-1] == '2' and str(ceil(year / 100))[-2] != '1':
    suffix = 'nd'
  elif str(ceil(year / 100))[-1] == '3' and str(ceil(year / 100))[-2] != '1':
    suffix = 'Rd'
  return str(ceil(year / 100)) + '{} century'.format(suffix)

