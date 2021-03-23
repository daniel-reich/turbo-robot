"""


Write a function that takes an integer `minutes` and converts it to seconds.

### Examples

    convert(5) ➞ 300
    
    convert(3) ➞ 180
    
    convert(2) ➞ 120

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def convert(minutes):
  sec = 60 * minutes
  return sec
  
print( convert(5))

