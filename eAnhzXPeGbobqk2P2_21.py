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

def century(y):
  t, h = map(int, [str(y)[0:2], str(y)[2:]])
  c = str(t+1 if h else t)
  return '{} century'.format(c+'st' if c == '21' else c+'th')

