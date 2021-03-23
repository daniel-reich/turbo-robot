"""


Jake is a very habitual person. He eats breakfast at 7:00 a.m. each morning,
lunch at 12:00 p.m. and dinner at 7:00 p.m. in the evening.

Create a function that takes in the current time as a string and determines
the duration of time before Jake's next meal. Represent this as a list with
the first and second elements representing hours and minutes, respectively.

### Examples

    time_to_eat("2:00 p.m.") ➞ [5, 0]
    // 5 hours until the next meal, dinner
    
    time_to_eat("5:50 a.m.") ➞ [1, 10]
    // 1 hour and 10 minutes until the next meal, breakfast

### Notes

N/A

"""

day_minutes = 24*60
factor = day_minutes/24
meals = [factor*7, factor*12, factor*19]
​
def time_to_eat(current_time):
    time, during = current_time.split(' ')
    h, m = time.split(':')
​
    minutes = int(h)*60 + int(m)
    if during == 'p.m.':
        minutes += (day_minutes/2)
​
    remaining_to_meals = [meal - minutes for meal in meals]
    remaining_to_meals = list(map(lambda x: x <= 0 and x+day_minutes or x, remaining_to_meals))
​
    next_meal = int(sorted(remaining_to_meals)[0])
    return [next_meal//60, next_meal%60]

