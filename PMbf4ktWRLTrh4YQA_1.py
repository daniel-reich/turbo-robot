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

def add_n_days_to_a_date(date, days):
  d,m,y = int(date[:2]),int(date[2:4]),int(date[4:])
  for i in range(days):
    leap = y%4==0 and (y%100!=0 or y%400==0)
    if d==31 and m in [1,3,5,7,8,10,12]:
      if m==12:
        d,m,y = 1,1,y+1
      else:
        d,m = 1,m+1
    elif d==30 and m in [4,6,9,11]:
      d,m = 1,m+1
    elif d==28 and m==2 and not leap:
      d,m = 1,3
    elif d==29 and m==2 and leap:
      d,m = 1,3
    else:
      d+=1
  d,m,y = [str(i) for i in [d,m,y]]
  if len(d)==1:
    d='0'+d
  if len(m)==1:
    m='0'+m
  return str(d)+str(m)+str(y)

