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
  #double overtime = 30$ an hour
  total = 0
  for i in range(len(hours)):
    if i == 5 or i == 6:
      for i in range(1,hours[i]+1):
        if i > 8:
          total += 30
        else:
          total += 20
    else:
      if hours[i] > 8:
        for i in range(1,hours[i]+1):
          if i > 8:
            total += 15
          else:
            total += 10
      else:
        total += hours[i] * 10
  return total

