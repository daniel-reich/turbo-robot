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
  cen = (year - 1)//100 + 1
  
  suffix = "th"
  if cen >= 20:
    lastDigit = cen%10
    if lastDigit == 1:
      suffix = "st"
    elif lastDigit == 2:
      suffix = "nd"
    elif lastDigit == 3:
      suffix = "rd"
  
  return str(cen) + suffix + " century"

