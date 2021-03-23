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

import re
​
def time_to_eat(current_time):
    pattern=r'(\d+):(\d\d) (\w)\.\w\.'
​
    matches=re.findall(pattern,current_time)
    bf=7
    lunch=12
    dinner=7
    if (matches[0][2]=='p'):        
        if(int(matches[0][1])==00  and int(matches[0][0])<7 ):
            next_meal_hr=7-int(matches[0][0])
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
        if(int(matches[0][1])==00  and int(matches[0][0])==12 ):
            next_meal_hr=int(matches[0][0])-7
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
        else:
            if(int(matches[0][0])==12):
                next_meal_hr=12-6
            if(int(matches[0][0])<7):
                next_meal_hr=6-int(matches[0][0])
            if(int(matches[0][0])>7):
                next_meal_hr=18-int(matches[0][0])    
​
            next_meal_min=60-int(matches[0][1])
            return [next_meal_hr,next_meal_min]
    if (matches[0][2]=='a' and int(matches[0][0])<12 and int(matches[0][0])>7):
        if(int(matches[0][1])==0 ):
            next_meal_hr=12-int(matches[0][0])
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
​
        else:
            next_meal_hr=11-int(matches[0][0])
            next_meal_min=60-int(matches[0][1])
            return [next_meal_hr,next_meal_min]
​
    if (matches[0][2]=='a'):
        if(int(matches[0][1])==0  and int(matches[0][0])<7 ):
            next_meal_hr=7-int(matches[0][0])
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
        if(int(matches[0][1])==0  and int(matches[0][0])==12 ):
            next_meal_hr=12-5
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
        else:
            if(int(matches[0][0])==12):
                next_meal_hr=12-6
            if(int(matches[0][0])<7):
                next_meal_hr=6-int(matches[0][0])
            next_meal_min=60-int(matches[0][1])
            return [next_meal_hr,next_meal_min]

