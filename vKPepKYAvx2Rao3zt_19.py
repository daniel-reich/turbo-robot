"""


A built-in timer inside your car can count the length of your ride in
**minutes** and you have started your ride at `00:00`.

Given the number of minutes `n` at the end of the ride, calculate the current
time. Return the **sum of digits** that the digital timer in the format
`hh:mm` will show at the end of the ride.

### Examples

    car_timer(240) ➞ 4
    # 240 minutes have passed since 00:00, the current time is 04:00
    # Digits sum up is 0 + 4 + 0 + 0 = 4
    
    car_timer(808) ➞ 14
    
    car_timer(14) ➞ 5

### Notes

N/A

"""

def car_timer(n):
  h,m=divmod(n,60)
  sum_h=sum([int(x) for x in str(h)])
  sum_m=sum([int(x) for x in str(m)])
  return sum_h+sum_m

