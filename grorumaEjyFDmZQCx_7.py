"""


A wristband can have 4 patterns:

  1. **horizontal** : each item in a row is identical.
  2.  **vertical** : each item in each column is identical.
  3.  **diagonal left** : each item is identical to the one on it's upper left or bottom right.
  4.  **diagonal right** : each item is identical to the one on it's upper right or bottom left.

You are shown an **incomplete section** of a wristband.

Write a function that returns `True` if the section can be correctly
classified into one of the 4 types, and `False` otherwise.

### Examples

    is_wristband([
      ["A", "A"],
      ["B", "B"],
      ["C", "C"]
    ]) ➞ True 
    # Part of horizontal wristband.
    
    is_wristband([
      ["A", "B"],
      ["A", "B"],
      ["A", "B"]
    ]) ➞ True 
    # Part of vertical wristband.
    
    is_wristband([
      ["A", "B", "C"],
      ["C", "A", "B"],
      ["B", "C", "A"],
      ["A", "B", "C"]
    ]) ➞ True
    # Part of diagonal left wristband.
    
    is_wristband([
      ["A", "B", "C"],
      ["B", "C", "A"],
      ["C", "A", "B"],
      ["A", "B", "A"]
    ]) ➞ True
    # Part of diagonal right wristband.

### Notes

N/A

"""

def is_vertical(l):
  return all(map(lambda x: x==l[0],l))
def is_horizontal(l):
  lt=[list(x) for x in zip(*l)]
  return is_vertical(lt)
def is_diagonal_left(l):
  d=[]
  for i in range(len(l)):
    d.append([l[x+i][x] for x in range(0,min(len(l)-i,len(l[0])))])
  for i in range(1,len(l[0])):
    d.append([l[x][x+i] for x in range(0,min(len(l),len(l[0]))-i)])
  ds=map(lambda x: set(x),d)
  return all(map(lambda x: len(x)==1,ds))
def is_diagonal_right(l):
  d=[]
  for i in range(len(l)):
    d.append([l[x+i][len(l[0])-1-x] for x in range(0,min(len(l)-i,len(l[0])))])
  for i in range(1,len(l[0])):
    d.append([l[x][len(l[0])-1-x-i] for x in range(0,min(len(l),len(l[0]))-i)])
  ds=map(lambda x: set(x),d)
  return all(map(lambda x: len(x)==1,ds))
def is_wristband(l):
  return is_vertical(l) or is_horizontal(l) or is_diagonal_left(l) or is_diagonal_right(l)

