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

def weekly_salary(lst):
  weekly = 0
  end_week = 0
  weekly_overtime = 0
  end_week_overtime = 0
  daily = 0
  daily_overtime = 0
  end_result = 0
  end_overtime_result = 0
  for i in range(len(lst)):
    if i < 5:
      if lst[i] > 8:
        weekly_overtime += lst[i] - 8
      weekly += lst[i]
    elif i >= 5:
      if lst[i] > 8:
        end_week_overtime += lst[i] - 8
      end_week += lst[i]
  daily += (weekly - weekly_overtime) * 10
  daily_overtime += weekly_overtime * 15
  end_result += (end_week - end_week_overtime) * 20
  end_overtime_result += end_week_overtime * 30
  return daily + daily_overtime + end_result + end_overtime_result

