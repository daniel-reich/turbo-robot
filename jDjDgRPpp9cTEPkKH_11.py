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

def over_time(lst):
  start, finish, rate, mult = lst
  
  pay = 0
  if start < 17:
      pay += (min(17, finish) - start) * rate *1.00001
  if finish > 17:
      pay += (finish - max(17, start)) * rate * mult
      
  return '${:,.2f}'.format(pay)
