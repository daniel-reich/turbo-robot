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
  if [v, r, i].count(None) != 1: return "Invalid"
  try:
    return round(r * i, 2)
  except:
    try:
      return round(v / i, 2)
    except:
      return round(v / r, 2)

