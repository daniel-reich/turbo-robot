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
  if(damage < 0 or speed < 0):
    return "invalid"
  second = 1
  if(time == "minute"):
    second = 60
  if(time == "hour"):
    second = 60*60
  return second * damage * speed

