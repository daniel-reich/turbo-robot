"""


Write a function that calculates overtime and pay associated with overtime.

  * Working 9 to 5: regular hours
  * After 5pm is overtime

Your function gets a list with 4 values:

  * Start of working day, in decimal format, (24-hour day notation)
  * End of working day. (Same format)
  * Hourly rate
  * Overtime multiplier

Your function should spit out:

  * `$` \+ earned that day (rounded to the nearest hundreth)

### Examples

    over_time([9, 17, 30, 1.5]) ➞ "$240.00"
    
    over_time([16, 18, 30, 1.8]) ➞ "$84.00"
    
    over_time([13.25, 15, 30, 1.5]) ➞ "$52.50"

2nd example explained:

  * From 16 to 17 is regular, so `1 * 30` = 30
  * From 17 to 18 is overtime, so `1 * 30 * 1.8` = 54
  * `30 + 54` = $84.00

"""

import decimal
​
def over_time(parameters):
​
  start = parameters[0]
  end = parameters[1]
  rate = parameters[2]
  factor = parameters[3]
    
  standard_time = 0
  over_time = 0
​
  over_time  += (min(9, end) - start) if start < 9 else 0
  over_time += (end - max(17, start)) if end > 17 else 0
  standard_time = min(17, end) - max(9, start)
  
  if standard_time < 0:
    standard_time = 0
  
  value = decimal.Decimal((standard_time * rate) + (over_time * rate * factor)).\
    quantize(decimal.Decimal('1.00'), rounding=decimal.ROUND_HALF_UP)
  return '${:04.2f}'.format(value)

