"""


Write a function that takes two integers (`hours`, `minutes`), converts them
to seconds, and adds them.

### Examples

    convert(1, 3) ➞ 3780
    
    convert(2, 0) ➞ 7200
    
    convert(0, 0) ➞ 0

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def convert(hours, minutes):
  hour = 3600
  minute = 60
  return (hour * hours) + (minute * minutes)

