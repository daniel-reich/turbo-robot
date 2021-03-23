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

import datetime
days_until_2021 = lambda date : "{} day".format((datetime.date(2021, 1, 1) - datetime.datetime.strptime(date, '%m/%d/%Y').date()).days) if (datetime.date(2021, 1, 1) - datetime.datetime.strptime(date, '%m/%d/%Y').date()).days == 1 else "{} days".format((datetime.date(2021, 1, 1) - datetime.datetime.strptime(date, '%m/%d/%Y').date()).days)

