"""


Write a function that takes a list of `hours` and returns the total weekly
salary.

  * The input list `hours` is listed sequentially, ordered from Monday to Sunday.
  * A worker earns $10 an hour for the first 8 hours.
  * For every overtime hour, he earns $15.
  * On weekends, the employer pays double the usual rate, _regardless how many hours were worked previously that week_. For instance, 10 hours worked on a weekday would pay 80+30 = $110, but on a weekend it would pay 160+60 = $220.

### Examples

    weekly_salary([8, 8, 8, 8, 8, 0, 0]) ➞ 400
    
    weekly_salary([10, 10, 10, 0, 8, 0, 0]) ➞ 410
    
    weekly_salary([0, 0, 0, 0, 0, 12, 0]) ➞ 280

### Notes

Every element in the list is greater than or equal to 0.

"""

def weekly_salary(hours):
  sum1 = 0
  sum2 = 0
  a = 0
  ar1 = hours[:5]
  ar2 = hours[5:]
  for x in ar1:
    if x <= 8:
      sum1 += x*10
      x += 1
    else:
      a = x - 8
      sum1 += a * 15 + (x - a) * 10
      a = 0
      x += 1
  for y in ar2:
    if y <= 8:
      sum2 += y*20
      x += 1
    else:
      a = y - 8
      sum2 += a * 30 + (y - a) * 20
      a = 0
      y += 1
  return sum2 + sum1

