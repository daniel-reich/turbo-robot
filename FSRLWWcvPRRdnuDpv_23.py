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

def time_to_eat(time: str) -> list:
    meals = (7, 12, 19)
    temp = [int(i) for i in time.split()[0].split(':')]
    if 'p.m.' in time:
        temp[0] += 12
​
    if temp[0] < meals[0]:
        if temp[1] == 0:
            return [meals[0] - temp[0], temp[1]]
        else:
            return [meals[0] - temp[0] - 1, 60 - temp[1]]
    elif temp[0] < meals[1]:
        if temp[1] == 0:
            return [meals[1] - temp[0], temp[1]]
        else:
            return [meals[1] - temp[0] - 1, 60 - temp[1]]
    elif temp[0] < meals[2]:
        if temp[1] == 0:
            return [meals[2] - temp[0], temp[1]]
        else:
            return [meals[2] - temp[0] - 1, 60 - temp[1]]
    else:
        if temp[1] == 0:
            return [meals[0] + 24 - temp[0], temp[1]]
        else:
            return [meals[0] + 24 - temp[0] - 1, 60 - temp[1]]

