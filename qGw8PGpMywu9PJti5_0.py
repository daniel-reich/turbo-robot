"""


You have three rods numbered from 1 to 3. A few disks of different sizes are
strung on the first rod. Disks are ranged by size from the smallest one on top
to the largest at the bottom.

Create a function that shows how to transfer the entire stack of `n` disks
from first to the third rod, obeying the following rules:

  1. Each move consists of taking the upper disk from one rod and placing it on another rod.
  2. No larger disk may be placed on top of a smaller disk.

The function should return a list of moves. Each move is represented by a
tuple of two numbers: the number of the rod from which to take the disk, and
the number of the rod where to put it.

### Examples

    hanoi(1) ➞ [(1, 3)]
    
    hanoi(2) ➞ [(1, 2), (1, 3), (2, 3)]
    
    hanoi(4) ➞ [(1, 2), (1, 3), (2, 3), (1, 2), (3, 1), (3, 2), (1, 2), (1, 3), (2, 3), (2, 1), (3, 1), (2, 3), (1, 2), (1, 3), (2, 3)]

### Notes

  * Function have to return an empty list if `n == 0`
  * The best way to solve this problem is to use recursion.

![GIF of the puzzle](https://edabit-
challenges.s3.amazonaws.com/Tower_of_Hanoi_4.gif)

"""

def hanoi(n):
  l=[]
  def f(n,s,d,a):
    if n==1:l.append((s,d));return
    f(n-1,s,a,d)
    l.append((s,d))
    f(n-1,a,d,s)
  if n>0:f(n,1,3,2)
  return l

