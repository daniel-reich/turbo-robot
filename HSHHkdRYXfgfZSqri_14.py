"""


Create a function that takes `damage` and `speed` (attacks per second) and
returns the amount of damage after a given `time`.

### Examples

    damage(40, 5, "second") ➞ 200
    
    damage(100, 1, "minute") ➞ 6000
    
    damage(2, 100, "hour") ➞ 720000

### Notes

Return "invalid" if `damage` or `speed` is negative.

"""

def damage(damage, speed, time):
  n = damage*speed
  return "invalid" if min(damage,speed)<0 else n*60 if time=="minute" else n*3600 if time == "hour" else n

