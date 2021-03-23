"""


From point _A_ , an object is moving towards point _B_ at constant velocity
`va` (in km/hr). From point _B_ , another object is moving towards point _A_
at constant velocity `vb` (in km/hr). Knowing this and the distance between
point _A_ and _B_ (in km), write a function that returns how much time passes
until both objects meet.

Format the output like this:

    "2h 23min 34s"

### Examples

    lets_meet(100, 10, 30) ➞ "2h 30min 0s"
    
    lets_meet(280, 70, 80) ➞ "1h 52min 0s"
    
    lets_meet(90, 75, 65) ➞ "0h 38min 34s"

### Notes

Seconds should be rounded down to the nearest whole number.

"""

def lets_meet(distance, va, vb):
    c = (va + vb)
    x = distance / c
    seconds = x * 60 * 60
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    #a="%2dh%02dmin%2ds" % (hours, minutes, seconds)
    result = ('{}h {}min {}s'.format(int(hours), int(minutes),int(seconds)))
​
    return result

