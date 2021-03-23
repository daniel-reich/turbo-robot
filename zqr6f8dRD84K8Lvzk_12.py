"""


As stated on the [On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A003215):

> The hexagonal lattice is the familiar 2-dimensional lattice in which each
> point has 6 neighbors.

A **centered hexagonal number** is a centered figurate number that represents
a hexagon with a dot in the center and all other dots surrounding the center
dot in a hexagonal lattice.

At the end of that web page the following illustration is shown:

    Illustration of initial terms:
    .
    .                                 o o o o
    .                   o o o        o o o o o
    .         o o      o o o o      o o o o o o
    .   o    o o o    o o o o o    o o o o o o o
    .         o o      o o o o      o o o o o o
    .                   o o o        o o o o o
    .                                 o o o o
    .
    .   1      7          19             37
    .

Write a function that takes an integer `n` and returns `"Invalid"` if `n` is
not a **centered hexagonal number** or its illustration as a multiline
rectangular string otherwise.

### Examples

    hex_lattice(1) ➞ " o "
    # o
    
    hex_lattice(7) ➞ "  o o  \n o o o \n  o o  "
    #  o o
    # o o o
    #  o o
    
    hex_lattice(19) ➞ "   o o o   \n  o o o o  \n o o o o o \n  o o o o  \n   o o o   "
    #   o o o
    #  o o o o
    # o o o o o
    #  o o o o
    #   o o o
    
    hex_lattice(21) ➞ "Invalid"

### Notes

N/A

"""

# y = 3x^2 + 3x + 1
# Quadratic formula: (12y-3)**0.5 - 3 must be divisible by 6, to be valid
​
def hex_lattice(y):
  if y == 1:
    return ' o '
    
  x = ( -3 + ( 12*y - 3 ) ** 0.5 ) / 6
  
  if x%1 != 0:
    return 'Invalid'
    
  else:
    lattice = ''
    top_row = int(x+1)
    widest_row = int(2*x+1)
    
    for i in range(top_row, widest_row+1):   # top half of lattice, including widest row
      lattice += ( ' '*(widest_row - i + 1) + 'o '*i + ' '*(widest_row - i) + '\n' )
    
    for i in range(widest_row-1, top_row, -1):   # bottom half of lattice, except last
      lattice += ( ' '*(widest_row - i + 1) + 'o '*i + ' '*(widest_row - i) + '\n' )
    lattice +=  ' '*(widest_row - top_row + 1) + 'o '*top_row + ' '*(widest_row - top_row) 
  return lattice

