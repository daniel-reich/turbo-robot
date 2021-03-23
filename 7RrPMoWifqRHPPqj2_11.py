"""


Traditional safes use a three-wheel locking mechanism, with the safe
combination entered using a dial on the door of the safe. The dial is marked
with clockwise increments between 0 and 99. The three-number combination is
entered by first dialling to the right (clockwise), then to the left (anti-
clockwise), and then to the right (clockwise) again. Combination numbers are
read from the top of the dial:

![](https://edabit-challenges.s3.amazonaws.com/image25.png)

Given the starting (top) position of the dial and the increments used for each
turn of the dial, return a list containing the _combination_ of the safe.

### Step-By-Step Example

    safecracker(0, [3, 10, 5]) ➞ [97, 7, 2]
    
    Starting dial position of 0 (same as the diagram above).
    
    First turn (rightward) of 3 increments:
    0 -> 99, 98, 97
    First number of combination = 97
    
    Second turn (leftward) of 10 increments:
    97 -> 98, 99, 0, 1, 2, 3, 4, 5, 6, 7
    Second number of combination = 7
    
    Third turn (rightward) of 5 increments:
    7 -> 6, 5, 4, 3, 2
    Third number of combination = 2
    
    The final combination is [97, 7, 2]

### Other Examples

    safecracker(96, [54, 48, 77]) ➞ [42, 90, 13]
    
    safecracker(43, [51, 38, 46]) ➞ [92, 30, 84]
    
    safecracker(4, [69, 88, 55]) ➞ [35, 23, 68]

### Notes

Each of the three combination numbers will be different.

"""

def highOrLow(x):
  if x > 99:
    x = x - 100
    return x
  elif x < 0:
    x = x + 100
    return x
  else:
    return x
  
def safecracker(start, increments):
  a = increments[0]
  b = increments[1]
  c = increments[2]
​
  aa = start - a
  aa = highOrLow(aa)
  bb = aa + b
  bb = highOrLow(bb)
  cc = bb - c
  cc = highOrLow(cc)
  return [aa, bb, cc]

