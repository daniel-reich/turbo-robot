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

months_31_days = [1,3,5,7,8,10,12];
def add_n_days_to_a_date(date, days):
    year = int(date[-4:]);
    month = int(date[2:4]);
    day = int(date[:2]);
    
    for i in range(days):
        day += 1;
        if(day == 32 and month == 12):
            day=1;
            month =1;
            year += 1;
        elif(month == 2):
            if((isLeapYear(year) == False and day == 29) or
                  (isLeapYear(year) and day == 30)):
                day =1;
                month += 1;
        elif((day == 31 and month not in months_31_days) or
            (day == 32 and month in months_31_days)):
            day = 1;
            month+=1;
       
    return str(day).zfill(2) + str(month).zfill(2) + str(year);
    
def isLeapYear(year):
    if(year % 4 == 0):
        if(year % 100 !=0 or year % 400 == 0):
            return True;
    return False;

