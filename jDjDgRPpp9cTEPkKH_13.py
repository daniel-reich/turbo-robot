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

def over_time(lst, half_up_round=0.001):
    checkin, checkout, rate, ot_multi = lst
    regular = max(min(17, checkout) - max(9, checkin), 0) * rate
    extra = max(checkout - max(17, checkin), 0) * rate * ot_multi
    return '${0:.2f}'.format(regular + extra + half_up_round, 2)

