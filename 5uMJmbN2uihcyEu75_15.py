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
    x = 0
    for i in range(0,5):
        if hours[i] > 8:
            x += 15 * ( hours[i] - 8 ) + 80
        else:
            x += 10 * hours[i]
    for j in range(5,7):
        if hours[j] > 8:
            x += 30 * ( hours[j] - 8 ) + 160
        else:
            x += 20 * hours[j]
    return x

