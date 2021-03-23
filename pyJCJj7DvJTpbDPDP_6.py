"""


Your task is to calculate the number of **days** between two dates. The dates
will be in the format **DDMMYYYY**. You are **not** allowed to import any
modules, especially the datetime module. The days will not include the end
date in calculation.

Remember to consider all leap years and leap months. The order of the larger
date and smaller date don't matter, as the days between them are the same
anyways.

### Examples

    days_between_dates("01012020", "02012020") ➞ 1
    
    days_between_dates("03101999", "02023000") ➞ 365,365
    
    days_between_dates("03101534", "07013443") ➞ 696,969
    
    days_between_dates("30012020", "01012020") ➞ 29

### Notes

  * Take note that a leap year is divisible by 4. However, if it is a new century (like 1900, 2400, etc), check its divisibility by 400. If it doesn't divvy into a whole number, then it is not a leap year (1900 isn't a leap year but 2400 is).
  * Do comment if there are any bugs or problems.

"""

def days_between_dates(d1, d2):
    
    if (d1[4:] + d1[0:2] + d1[2:4]) > (d2[4:] + d2[0:2] + d2[2:4]):
        d1, d2 = d2, d1
​
    cnt_yrs = 0
    cnt_mths_d1 = 0 + int(d1[0:2])
    cnt_mths_d2 = 0 + int(d2[0:2])
​
    dict_norm = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
                 '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    dict_leap = {'1': 31, '2': 29, '3': 31, '4': 30, '5': 31, '6': 30,
                 '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
​
    for i in range(1, int(d1[2:4])):
        if d1[6:] == '00' and int(d1[4:]) % 400 == 0:
            cnt_mths_d1 += dict_leap[str(i)]
        elif d1[6:] != '00' and int(d1[4:]) % 4 == 0:
            cnt_mths_d1 += dict_leap[str(i)]
        else:
            cnt_mths_d1 += dict_norm[str(i)]
​
    for i in range(1, int(d2[2:4])):
        if d2[6:] == '00' and int(d2[4:]) % 400 == 0:
            cnt_mths_d2 += dict_leap[str(i)]
        elif d2[6:] != '00' and int(d2[4:]) % 4 == 0:
            cnt_mths_d2 += dict_leap[str(i)]
        else:
            cnt_mths_d2 += dict_norm[str(i)]
​
    for i in range(min(int(d1[4:]),int(d2[4:])), max(int(d1[4:]),int(d2[4:]))):
        if str(i)[len(str(i))-2:] == '00' and i % 400 == 0:
            cnt_yrs += 366
        elif str(i)[len(str(i))-2:] != '00' and i % 4 == 0:
            cnt_yrs += 366
        else:
            cnt_yrs += 365
​
    return cnt_yrs - cnt_mths_d1 + cnt_mths_d2

