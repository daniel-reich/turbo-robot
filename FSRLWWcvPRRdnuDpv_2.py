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
    
    time = current_time.split()
    hours = time[0].split(':')[0]
    minutes = time[0].split(':')[1]
    
    ret = [0,0]
    
    if hours == '12' or hours == '11':
        if minutes == '00':
            ret[0] = abs(ret[0] - 7)
        else:
            ret[0] = abs(ret[0] - 6)
            ret[1] += (60 - int(minutes))
        
    if int(hours) < 7:
        if minutes == '00':
            ret[0] += (7 - int(hours))
        else:
            ret[0] += (6 - int(hours))
            ret[1] += (60 - int(minutes))
​
    if time[-1] == 'a.m.' and 7 <= int(hours) <= 10:
        if minutes == '00':
            ret[0] += (12 - int(hours))
        else: 
            ret[0] += (11 - int(hours))
            ret[1] += (60 - int(minutes))
    
    if hours == '11':
        ret[0] += 1
        
    return ret

