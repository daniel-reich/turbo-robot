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

def time_to_eat(ct):
    h, p = int(ct[:ct.find(':')]), ct[ct.find('.')-1]=='p'
    m = int(ct[ct.find(':')+1:ct.find(' ')])
    h = 7-h-int(m>0) if p else 12-h-int(m>0) if 7<=h<12 else 7-h-int(m>0)
    m = 60 - m if m > 0 else m
    return [h if h>=0 else 12+h ,m]

