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

import datetime
def time_to_eat(current_time):
    col_index = current_time.index(':')
    h = int(current_time[:col_index])
    if current_time[col_index+4] == 'p':
        h += 12
    m = int(current_time[col_index+1:col_index+3])
    ct = datetime.time(h,m)
    ctm = h*60+m
    t1 = datetime.time(7)
    t1m = 7*60
    t2 = datetime.time(12)
    t2m = 12*60
    t3 = datetime.time(19)
    t3m = 19*60
    #meals = [t1,t2,t3]
    if ctm < t1m:
        return [int((t1m-ctm)/60),(t1m-ctm)%60]
    if ctm < t2m:
        return [int((t2m-ctm)/60),(t2m-ctm)%60]
    if ctm < t3m:
        return [int((t3m-ctm)/60),(t3m-ctm)%60]
    else:
        return [int((t1m+24*60-ctm)/60),(t1m+24*60-ctm)%60]

