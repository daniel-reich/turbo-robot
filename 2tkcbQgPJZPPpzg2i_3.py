"""


What do the digits 0, 4, 6, 8, and 9 have in common? Well, they are whole
numbers... and they are also _hole_ numbers (not actually a thing until now).
Hole numbers are numbers with holes in their shapes (8 is special in that it
contains two holes).

14 is a hole number with one hole. 88 is a hole number with four holes.

Your task is to create a function with argument `N` that returns the sum of
the holes for the integers _n_ in the range of range _0 < n <= N_.

To illustrate, `sum_of_holes(14)` returns `7`, because there are 7 holes in 4,
6, 8, 9, 10 and 14.

### Examples

    sum_of_holes(4) ➞ 1
    
    sum_of_holes(6) ➞ 2
    
    sum_of_holes(8) ➞ 4
    
    sum_of_holes(6259) ➞ 12345

### Notes

  * All test cases are positive real integers.
  * Don't forget that 8 has two holes.

"""

def sum_of_holes(N):
  one = "4690"
  two = "8"
  holes = 0
  for i in range(1, N+1):
    i = str(i)
    for j in i:
      if j in one:
        holes+=1
      elif j in two:
        holes +=2
  return holes

