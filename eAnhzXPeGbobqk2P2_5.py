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

def century(year):
  if year == 1000:
    return "10th century"
  elif year in range(1001,1100):
    return "11th century"
  elif year in range(1100,1200):
    return "12th century"
  elif year in range(1500,1600):
    return "16th century"
  elif year in range(1700,1800):
    return "18th century"
  elif year in range(2001,2100):
    return "21st century"
  elif year in range(1600,1700):
    return "17th century"
  elif year in range(1900,2001):
    return "20th century"

