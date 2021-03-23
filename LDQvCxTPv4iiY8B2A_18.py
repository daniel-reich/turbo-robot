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
  return ntxt[::-1] == "".join(i if i not in "69" else "9" if i=="6" else "6" for i in ntxt)
