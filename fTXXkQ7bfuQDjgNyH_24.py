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
    dict= {1: 31 , 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    date = date.split('/')
    day=0
    for i in dict:
        if i==int(date[0]):
            break
        day+=dict[i]
    day+=int(date[1])
    if int(date[2])%100==0:
        if int(date[2])%400==0 and int(date[0])>2:
            return day+1
        else:
            return day
    else:
        if int(date[2])%4==0 and int(date[0])>2:
            return day+1
        else:
            return day

