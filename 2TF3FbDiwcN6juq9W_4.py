"""


Given a `date`, return how many days `date` is away from 2021 (end date not
included). `date` will be in **mm/dd/yyyy** format.

### Examples

    days_until_2021("12/28/2020") ➞ "3 days"
    
    days_until_2021("1/1/2020") ➞ "366 days"
    
    days_until_2021("2/28/2020") ➞ "308 days"

### Notes

All given dates will be in the year 2020.

"""

from datetime import date as d
​
def days_until_2021(date):
    date = list(map(lambda x:int(x),date.split('/')))[::-1]
    ans =  ((d(2021,1,1)-d(date[0],date[2],date[1])).days)
    return str(ans)+' days' if ans!=1 else str(ans) + ' day'

