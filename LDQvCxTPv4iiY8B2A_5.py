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
  def swap69(txt):
    return txt.replace("6", "x").replace("9", "6").replace("x", "9")
  if ntxt == "0":
    return True
  if len(ntxt) % 2 and ntxt[len(ntxt)//2] != "0":
    return False
  first_half = ntxt[:(len(ntxt)//2)]
  second_half = ntxt[-(len(ntxt)//2):]
  return  first_half == swap69(second_half[::-1])

