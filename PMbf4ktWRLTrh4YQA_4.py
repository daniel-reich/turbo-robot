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
  d,m,y = int(date[:2]), int(date[2:4]), int(date[4:])
  
  def month_days(m,y):
    dic={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    return dic[m] + (1*(y%4==0) -1*(y%100==0) +1*(y%400==0))*(m==2)
    
  def adv_one(d,m,y):
    if (d,m) == (31,12): return (1,1,y+1)
    if d == month_days(m,y): return (1,m+1,y)
    return (d+1,m,y)
  
  for i in range(days): d,m,y = adv_one(d,m,y)
  
  d,m,y = str(d),str(m),str(y)
​
  return "0"*(2-len(d))+d+"0"*(2-len(m))+m+y

