"""


Create a function that takes a 2D array as an argument and returns the number
of people whose view is blocked by a tall person. The concert stage is pointed
towards the top of the 2D array and the tall person (represented by a 2)
blocks the view of all the people (represented by a 1) behind them.

### Examples

    block([
      [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 2],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1]
    ]) ➞ 2
    
    # The tall person blocks 2 people behind him thus
    # the function returns 2.
    block([
      [1, 2, 1, 1],
      [1, 1, 1, 2],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
    ]) ➞ 5
    
    # There are 2 tall people that block everyone behind
    # them. The first tall person in the first row blocks 3
    # people behind him while the second tall person in
    # the second row blocks 2 people behind him thus the
    # function returns 5.
    block([
      [1, 1, 1, 1],
      [2, 1, 1, 2],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
    ]) ➞ 4

### Notes

  1. There is only a maximum of 1 tall person in every column.
  2. No view is blocked if the tall person is in the last row.

"""

def block(lst):
    x=[]
    for i in lst:
        for j in i:
            if j==2:
                if lst.index(i)!=len(lst)-1:
                    x.append((lst.index(i)))
    return sum([abs(i-len(lst))-1 for i in x])

