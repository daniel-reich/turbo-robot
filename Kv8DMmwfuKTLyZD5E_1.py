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

def entry(r,c):
  return min(r,c) + 1 
def convert(lst):
  string = [str(el) for el in lst]
  return ''.join(string)
def make_dartboard(n):
  lst = [[entry(i,j) for j in range(0,n//2)] for i in range(0,n//2)]
  for i in range(0,len(lst)):
    lst[i].extend(lst[i][::-1])
    if n % 2 == 1:
      lst[i].insert(n//2,i+1)
  lst.extend(lst[::-1])
  if n % 2 == 1:
    lst.insert(n//2,list(range(1,n//2 + 1)))
    lst[n//2].extend(list(range(1,n//2 + 1))[::-1])
    lst[n//2].insert(n//2,n//2 + 1)
  return list(map(lambda x: int(convert(x)),lst))

