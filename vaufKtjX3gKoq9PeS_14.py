"""


Create a function that calculates the missing value of 3 inputs using Ohm's
law. The inputs are `v`, `r` or `i` (aka: voltage, resistance and current).

Ohm's law:

    V = R * I

Return the missing value rounded to two decimal places.

### Examples

    ohms_law(12, 220, None) ➞ 0.05
    
    ohms_law(230, None, 2) ➞ 115
    
    ohms_law(None, 220, 0.02) ➞ 4.4
    
    ohms_law(None, None, 10) ➞ "Invalid"
    
    ohms_law(500, 50, 10) ➞ "Invalid"

### Notes

  * Missing values will be `None`
  * If there is more than one missing value, or no missing value, return `"Invalid"`
  * Only numbers will be given.

"""

def ohms_law(v, r, i):
  
  Parameters = []
  Parameters.append(v)
  Parameters.append(r)
  Parameters.append(i)
  
  if (Parameters.count(None) >= 2):
    return "Invalid"
  elif (v == None):
    return round(r * i, 2)
  elif (r == None):
    return round(v / i, 2)
  elif (i == None):
    return round(v / r, 2)
  else:
    return "Invalid"

