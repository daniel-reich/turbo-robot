"""


An employee working at a very bizzare company, earns one penny on their first
day. However, for every day that passes, their base amount **doubles** , so
they earn two pennies on the second day and four pennies on the third day
(totalling 7 pennies). Given a number of days, return how many pennies the
employee accumulates.

### Examples

    doubled_pay(1) ➞ 1
    
    doubled_pay(2) ➞ 3
    
    doubled_pay(3) ➞ 7

### Notes

You will only get tests for valid positive integers.

"""

def doubled_pay(n):
  def pay_day(n):
    if n == 1:
      return 1
    else:
      return pay_day(n-1) * 2
  
  pay = 0
  
  for num in range(1, n+1):
    pay += pay_day(num)
    #print(num, pay_day(num))
  
  return pay

