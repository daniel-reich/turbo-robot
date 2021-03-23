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

def time_to_eat(current_time):
    #changing the string to a list
    current_time = current_time.replace(' ', ':')
    current_time = current_time.split(':')
​
    #changing hours and minutes to integers
    current_time[0] = int(current_time[0])
    current_time[1] = int(current_time[1])
​
    #7AM and 7PM are both meal times
    if current_time[0] == 7 and current_time[1] == 0:
        hours = 0
        minutes = 0
        return [hours, minutes]
​
    #different conditions for AM
    elif 'a.m.' in current_time:
        if current_time[0] < 7:
            hours = 7 - current_time[0]
            if current_time[1] == 0:
                minutes = 0
                return [hours, minutes]
            else:
                hours -= 1
                minutes = 60 - current_time[1]
                return [hours, minutes]
​
        elif current_time[0] == 12:
            hours = 7
            minutes = 0
            return [hours, minutes]
        else:
            hours = 12 - current_time[0]
            if current_time[1] == 0:
                minutes = 0
                return [hours, minutes]
            else:
                hours -= 1
                minutes = 60 - current_time[1]
                return [hours, minutes]
​
​
    if 'p.m.' in current_time:
        if current_time[0] == 12 and current_time[1] == 0:
            hours = 0
            minutes = 0
            return [hours, minutes]
        elif current_time[0] < 7:
            hours = 7 - current_time[0]
            if current_time[1] == 0:
                minutes = 0
                return [hours, minutes]
            else:
                hours -= 1
                minutes = 60 - current_time[1]
                return [hours, minutes]
        else:
            hours = 7 + (12 - current_time[0])
            if current_time[1] == 0:
                 minutes = 0
                 return [hours, minutes]
            else:
                hours -= 1
                minutes = 60 - current_time[1]
                return [hours, minutes]

