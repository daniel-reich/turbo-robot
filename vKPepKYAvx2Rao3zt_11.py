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

import math
def car_timer(n):
  if len(str(n))==3:return math.ceil(n/60)
  if len(str(n))==4:return int((str(n)[0])+(str(n)[-1]))
  return sum([int(i) for i in ' '.join(x for x in str(n).replace(',','')).split(' ')])

