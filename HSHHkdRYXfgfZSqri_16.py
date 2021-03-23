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

def damage(damage,speed,time):
    result = damage * speed
    if damage > 0 and speed > 0:
        if time == "second":
            result1 = result*1
            return result1
        elif time == 'minute':
            result1 = result * 60
            return result1
        elif time == 'hour':
            result1 = result * 3600
            return result1
    else:
        return "invalid"

