"""


Create a function that returns the date in **DDMMYYYY** format after a
specific date. Consider leap years and leap months (e.g. February 29th).
Please **do not import** anything (such as `datetime`).

### Examples

    add_n_days_to_a_date("15041984", 6038) ➞ "26102000"
    
    add_n_days_to_a_date("26102000", 6038)) ➞ "08052017"
    
    add_n_days_to_a_date("01011900", 30) ➞ "31011900"

### Notes

  * Remember that if the year is a new century like 1800, although it is divisible by 4, it isn't divisible by 400, hence it's NOT a leap year.
  * Please give feedback if there are any bugs (this is my first time making a challenge).

"""

def leap_days(y):
    return 29 if y%400 == 0 or (y%4 == 0 and y%100 != 0) else 28
​
def add_n_days_to_a_date(date, days):
    d, m, y = int(date[:2]), int(date[2:4]), int(date[-4:])
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days += d
    
    while True:
        if m == 2:
            months[1] = leap_days(y)
        if days <= months[m-1]:
            return '{:02}{:02}{}'.format(days, m, y)
        days -= months[m-1]
        if m == 12:
            y += 1
            m = 1
        else:
            m += 1

