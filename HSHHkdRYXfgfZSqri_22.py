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
  if damage < 0 or speed < 0:
    return "invalid"
  elif time == "second":
    return damage*speed
  elif time == "minute":
    return damage*speed*60
  elif time == "hour":
    return damage*speed*3600

