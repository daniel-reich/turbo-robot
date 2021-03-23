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
  end,out,out1 = n//2 +1 if n%2==1 else n//2, [[1]*n],[]
  for i in range (1,end):
    row=[]
    positions=[i for i in range (n)]
    for j in range (i):
      positions.pop(0)
      positions.pop(-1)
    for k in range (n):
      if (k in positions):
        row.append(out[i-1][k]+1)
      else:
        row.append(out[i-1][k])
    out.append(row)
  for i in range (n//2-1,-1,-1):
    out.append(out[i])
  for i in range (len(out)):
    s=''
    for j in range (len(out)):
      s+=str(out[i][j])
    out1.append(int(s))
  return out1

