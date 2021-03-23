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

def damage(dam, speed, time):
    if dam< 0 or speed < 0:
        return "invalid"
    timedict = {"second":1, "minute":60, "hour":3600}
    return(speed*(timedict[time])*dam)

