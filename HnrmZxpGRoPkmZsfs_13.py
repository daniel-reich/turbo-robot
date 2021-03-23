"""


Given the parameters day, month and year, return whether that date is **a
valid date**.

### Examples

    is_valid_date(35, 2, 2020) ➞ False
    # February doesn't have 35 days.
    
    is_valid_date(8, 3, 2020) ➞ True
    # 8th March 2020 is a real date.
    
    is_valid_date(31, 6, 1980) ➞ False
    # June only has 30 days.

### Notes

Try using the `datetime` module to complete this challenge (see the
**Resources** tab for some tutorials on this).

"""

def is_valid_date(d, m, y):
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y%4==0 and (y%100 != 0 or y%400==0):
        day_count_for_month[2] = 29
    return (1 <= m <= 12 and 1 <= d <= day_count_for_month[m])

