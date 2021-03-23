"""


The number 6090609 has a special property: if you turn the number upside down
(imagine rotating your screen 180 degrees), you get 6090609 again.

Write a function that takes a string on the digits 0, 6, 9 and decides if the
number is the same upside down.

### Examples

    same_upsidedown("6090609") ➞ True
    
    same_upsidedown("9669") ➞ False
    # Becomes 6996 when upside down.
    
    same_upsidedown("69069069") ➞ True

### Notes

N/A

"""

def same_upsidedown(ntxt):
  upside_down = ""
  for char in ntxt[::-1]:
    if char == "6":
      upside_down += "9"
    elif char == "9":
      upside_down += "6"
    else:
      upside_down += char
  return ntxt == upside_down

