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

from datetime import date
​
def days_until_2021(d):
    M, D, Y = d.split('/')
    days = str((date(2021, 1, 1) - date(int(Y), int(M), int(D))).days)
    return days + ' days' if days != '1' else days + ' day'

