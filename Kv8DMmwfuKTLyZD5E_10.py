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

def make_dartboard(n):
  if n == 1:
    return [1]
  if n == 2:
    return [11,11]
  
  lines =["1"*n]
  for i in range(1,n//2+1):
    lines.append(lines[-1][:i] + "".join(list(map(lambda x: str(int(x)+1),lines[-1][i:-i]))) + lines[-1][-i:])
  if n%2 == 1:
    lines.extend(lines[:-1][::-1])
  else:
    lines.extend(lines[:-2][::-1])
  return list(map(int,lines))

