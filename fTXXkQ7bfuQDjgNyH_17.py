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
    year_dct = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
                10: 31, 11: 30, 12: 31}
​
    date_split = date.split("/")
    month = date_split[0]
    day = date_split[1]
    year = date_split[-1]
    if ((int(year) % 100 == 0 and int(year) % 400 == 0) or (int(year) % 100 != 0 and int(year) % 4 == 0)) and int(month) > 2:
        return sum(year_dct[month] for month in range(1, int(month))) + int(day) + 1
    else:
         return sum(year_dct[month] for month in range(1, int(month))) + int(day)

