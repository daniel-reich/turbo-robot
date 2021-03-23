"""


Create a function which creates a square dartboard of side length `n`. The
value of a number should increase, the closer it is to the centre of the
board.

### Examples

    make_dartboard(3) ➞ [
      111,
      121,
      111
    ]
    
    make_dartboard(8) ➞ [
      11111111,
      12222221,
      12333321,
      12344321,
      12344321,
      12333321,
      12222221,
      11111111
    ]
    
    make_dartboard(5) ➞ [
      11111,
      12221,
      12321,
      12221,
      11111
    ]

### Notes

If the size given is an even number, the centre should be made up of the 4
highest values.

"""

from math import ceil
def make_dartboard(n):
  if n == 1: return [1]
  db, c = [], ceil(n/2)
  for i in range(c):
    a = ''.join([str(j+1) for j in range(i)])
    db.append(int(a + str(i+1)*(n - len(a)*2) + a[::-1]))
  return db + db[n//2-1::-1]

