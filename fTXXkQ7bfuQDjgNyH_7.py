"""


Each year has 365 or 366 days. Given a string `date` representing a Gregorian
calendar date formatted as `month/day/year`, return the _day-number_ of the
year.

### Examples

    day_of_year("11/16/2020") ➞ 321
    
    day_of_year("1/9/2019") ➞ 9
    
    day_of_year("3/1/2004") ➞ 61
    
    day_of_year("12/31/2000") ➞ 366

### Notes

All input strings in tests are valid dates.

"""

def day_of_year(date):
    days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    d= list(map(int,date.split("/")))
    if d[2] % 400 == 0:
         days[2]+=1
    elif d[2]%4 == 0 and d[2]%100!=0:
         days[2]+=1
    for i in range(1,len(days)):
         days[i]+=days[i-1]         
    return days[d[0]-1]+d[1]

