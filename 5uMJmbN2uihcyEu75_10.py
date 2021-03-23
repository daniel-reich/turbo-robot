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
  salary = 0
  for idx, hours_day in enumerate(hours):
    if idx in [5,6]:
      if hours_day > 8:
        salary += (8*10+(hours_day-8)*15)*2
      else:
        salary += (10*hours_day)*2
    else:
      if hours_day > 8:
        salary += 8*10+(hours_day-8)*15
      else:
        salary +=10*hours_day
  return salary

