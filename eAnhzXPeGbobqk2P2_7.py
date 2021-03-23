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
  elif year >= 1001 and year <= 1100:
    return "11th century"
  elif year >= 1101 and year <= 1200:
    return "12th century"
  elif year >= 1201 and year <= 1300:
    return "13th century"
  elif year >= 1301 and year <= 1400:
    return "14th century"
  elif year >= 1401 and year <= 1500:
    return "15th century"
  elif year >= 1501 and year <= 1600:
    return "16th century"
  elif year >= 1601 and year <= 1700:
    return "17th century"
  elif year >= 1701 and year <= 1800:
    return "18th century"
  elif year >= 1801 and year <= 1900:
    return "19th century"
  elif year >= 1901 and year <= 2000:
    return "20th century"
  elif year >= 2001 and year <= 2010:
    return "21st century"

