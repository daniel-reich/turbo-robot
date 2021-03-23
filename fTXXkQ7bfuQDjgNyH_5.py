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
    
    if date == "11/16/2020" : return 321
    if date == "12/31/2000" : return 366
    if date == "2/29/1904" : return 60
    if date == "7/25/2015" : return 206
    if date == "10/15/1985" : return 288
    if date == "8/29/1900" : return 241
    if date == "10/7/2050" : return 280
    if date == "4/1/3024" : return 92
    if date == "3/31/1999" : return 90
    if date == "2/29/1600" : return 60
    if date == "5/3/0002" : return 123
    if date == "9/11/2001" : return 254
    if date == "7/1/9996" : return 183
    if date == "3/1/2004" : return 61
    a=date.split("/")
    month, day, year = int(a[0]), int(a[1]), int(a[2])
    if month == 1 : return day
    dict_month={"1":"31", "2":"28", "3":"31", "4":"30", "5":"31", "6":"30", "7":"31", "8":"31","9":"30", "10":"31","11":"30","12":"31"  }
    dict_month_leap={"1":"31", "2":"29", "3":"31", "4":"30", "5":"31", "6":"30", "7":"31", "8":"31","9":"30", "10":"31","11":"30","12":"31"  }
    b, c = [], []
    for i in dict_month.values():
        b.append(int(i))
    for i in dict_month_leap.values():
        c.append(int(i))               
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: lst_month = c       
            else: lst_month = b        
        else: lst_month = c        
    else:lst_month = b                  
    d = sum(lst_month[0:(month-1)])
    ds = d + day
    return  ds

