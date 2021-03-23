"""


In this challenge, sort a list containing a series of dates given as strings.
Each date is given in the format `DD-MM-YYYY_HH:MM`:

    "12-02-2012_13:44"

The priority of criteria used for sorting will be:

  * Year
  * Month
  * Day
  * Hours
  * Minutes

Given a list `lst` and a string `mode`, implement a function that returns:

  * if `mode` is equal to `"ASC"`, the list `lst` sorted in ascending order.
  * if `mode` is equal to `"DSC"`, the list `lst` sorted in descending order.

### Examples

    sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC") ➞ ["10-02-2016_12:30", "10-02-2018_12:15", "10-02-2018_12:30"]
    
    sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC") ➞ ["10-02-2018_12:30", "10-02-2018_12:15", "10-02-2016_12:30"]
    
    sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC") ➞ ["01-01-1999_00:55", "09-02-2000_10:03", "10-02-2000_18:29"]

### Notes

  * Remember: the date is in the format `DD-MM-YYYY_HH:MM`.
  * You can expect only valid formatted dates, without exceptions to handle.

"""

def insertions_sort(lst):
    has = True
    while has:
        has = False
        for indexex in range(1,len(lst)):
            current_number = lst[indexex]
            last_numer = lst[indexex-1]
            if last_numer > current_number:
                has = True
                temp = last_numer
                lst[indexex-1] = current_number
                lst[indexex] = temp
    return lst
​
def revers(lst):
    order_parts = []
    for parts in lst:
        order_parts.insert(0, parts)
    return order_parts
​
​
def sort_dates(lst, mode):
    times = {}
    for dates in lst:
        parts = dates.split("_")
        x = parts[0].split("-") + parts[1].split(":")
        orderd_times = int(x[2]+x[1]+x[0]+x[3]+x[4])
        times[orderd_times] = dates
    orderd_time = insertions_sort(list(times.keys()))
    list_of_orderd_times = []
    for things in orderd_time:
        list_of_orderd_times.append(times[things])
​
    if mode == "DSC":
        return revers(list_of_orderd_times)
    else:
        return list_of_orderd_times

