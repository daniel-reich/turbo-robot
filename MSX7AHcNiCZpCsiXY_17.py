"""


Create a function which returns how many **Friday 13ths** there are in a given
year.

### Examples

    how_unlucky(2020) ➞ 2
    
    how_unlucky(2026) ➞ 3
    
    how_unlucky(2016) ➞ 1

### Notes

Check **Resources** for some helpful tutorials on the Python `datetime`
module.

"""

def how_unlucky(yr):
    import datetime
    count = 0
    for mon in range(1, 13):
        for day in range(1, 32):
            try:
                x = datetime.date(yr, mon, day)
                if day == 13 and x.strftime("%A") == "Friday":
                    count += 1
            except ValueError:
                next
    return count

