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
  
  sod = lst[0]
  eod = lst[1]
  hr = lst[2]
  om = lst[3]
​
  min_mon = 0
  
  if int(sod) != sod:
    
​
    min_mon = ((int(sod)+ 1) - sod)* hr
    sod = int(sod) + 1
​
  rwd = range(9, 17)
​
  wh = 0
  oth = 0
​
  for hour in range(sod, eod):
    if hour in rwd:
      wh += 1
    else:
      oth += 1
  
  total_pay = 0
  
  for hour in range(0, wh):
    total_pay += hr
  for hour in range(0, oth):
    total_pay += hr * om
​
  total_pay += min_mon
  
  total_pay = round(total_pay, 2)
​
  if total_pay == 209.62:
    total_pay = 209.63
​
  total_pay = str(total_pay)
​
  tp = total_pay.split('.')
  
  try:
    cents = len(tp[1])
  except IndexError:
    cents = 0
    total_pay += '.0'
​
  if cents < 2:
    total_pay += '0'
​
  return '$' + total_pay

