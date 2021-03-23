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

def day_of_year(string):
    tmp=string.split("/")
    ev=int(tmp[2])
    nap=int(tmp[1])
    honap=int(tmp[0])
​
    sum=0
​
    flag=False
    def isLeapYear(string):
        if ev % 4 == 0 and ev % 100 != 0:
            return True
        if ev % 4 == 0 and ev % 100 == 0 and ev % 400 == 0:
            return True
​
    dict={'1':31,'2':'','3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
​
    if isLeapYear(ev) == True:
        dict['2']=29
    else:
        dict['2']=28
​
    for i in range(1,honap):
        tmp = dict[str(i)]
        sum+=tmp
    
    sum+=nap
    return sum

