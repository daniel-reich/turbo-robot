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
  result = ""
  if year == 1000:
    result += "10th"
  elif 1001 <= year <= 1100:
    result += "11th"
  elif 1101 <= year <= 1200:
    result += "12th"
  elif 1201 <= year <= 1300:
    result += "13th"
  elif 1301 <= year <= 1400:
    result += "14th"
  elif 1401 <= year <= 1500:
    result += "15th"
  elif 1501 <= year <= 1600:
    result += "16th"
  elif 1601 <= year <= 1700:
    result += "17th"
  elif 1701 <= year <= 1800:
    result += "18th"
  elif 1801 <= year <= 1900:
    result += "19th"
  elif 1901 <= year <= 2000:
    result += "20th"
  elif 2001 <= year <= 2010:
    result += "21st"
  return result + " century"

