"""


 **Mubashir** needs your help to construct a building which will be a pile of
`n` cubes. The cube at the bottom will have a volume of **n^3** , the cube
above will have volume of **(n-1)^3** and so on until the top which will have
a volume of **1^3**.

Given the total volume `m` of the building, can you find the number of cubes
`n` required for the building?

In other words, you have to return an integer `n` such that:

    n^3 + (n-1)^3 + ... + 1^3 == m

Return `None` if there is no such number.

### Examples

    pile_of_cubes(1071225) ➞ 45
    
    pile_of_cubes(4183059834009) ➞ 2022
    
    pile_of_cubes(16) ➞ None

### Notes

N/A

"""

def pile_of_cubes(m):
  c = 1
  r = m
  x = 0
  while x < m:
    x += c*c*c
    r -= c*c*c
    c += 1
  if r == 0: 
    y = c-1 
  else: 
    y = None
  return y

