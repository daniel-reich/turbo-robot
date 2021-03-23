"""


Create a function that accepts a measurement value in inches and returns the
equivalent of the measurement value in feet.

### Examples

    inches_to_feet(324) ➞ 27
    
    inches_to_feet(12) ➞ 1
    
    inches_to_feet(36) ➞ 3

### Notes

  * If inches are under 12, return `0`.
  * 12 inches = 1 foot.

"""

def inches_to_feet(inches):
    feet = inches / 12
    if feet < 1 :
        return 0
    return feet
​
​
game = inches_to_feet(14)
print(game)
