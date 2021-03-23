"""


One cause for speeding is the desire to shorten the time spent traveling. In
long distance trips speeding does save an appreciable amount of time. However,
the same cannot be said about short distance trips.

Create a function that calculates the amount of time saved were you traveling
with an average speed that is _above_ the speed-limit as compared to traveling
with an average speed _exactly at_ the speed-limit.

### Examples

    # The parameter's format is as follows:
    # (speed limit, avg speed, distance traveled at avg speed)
    
    time_saved(80, 90, 40) ➞ 3.3
    
    time_saved(80, 90, 4000) ➞ 333.3
    
    time_saved(80, 100, 40 ) ➞ 6.0
    
    time_saved(80, 100, 10) ➞ 1.5

### Notes

  * Speed = distance/time
  * The time returned should be in **minutes** , not hours.

"""

def time_saved(s_lim, s_avg, d):
  return round((d/s_lim-d/s_avg)*60,1)

