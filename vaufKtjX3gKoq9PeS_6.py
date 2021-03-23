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
    if len([i for i in [v,r,i] if i==None])>=2:return 'Invalid'
    if len([i for i in [v,r,i] if i!=None])>=3:return 'Invalid'
    if v==None:return min([i for i in [v,r,i] if  i!=None])*max([i for i in [v,r,i] if i!=None])
    if r==None:return round(max([i for i in [v,r,i] if i!=None])/min([i for i in [v,r,i] if i!=None]))
    if i==None:return round(min([i for i in [v,r,i] if i!=None])/max([i for i in [v,r,i] if i!=None]),2)

