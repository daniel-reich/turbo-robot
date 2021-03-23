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
  if time is "second":
    time = 1
  elif time is "minute":
    time = 60
  else:
    time = 3600
  if damage < 0 or speed < 0:
    return "invalid"
  else:
    return damage * speed * time

