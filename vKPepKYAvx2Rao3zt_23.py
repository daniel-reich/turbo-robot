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
  seconds = (n * 60) % (24 * 3600) 
  hour = seconds // 3600
  seconds %= 3600
  minutes = seconds // 60
  seconds %= 60   
  t = "%02d:%02d" % (hour, minutes) 
  return int(t[0]) + int(t[1]) + int(t[3]) + int(t[4])

