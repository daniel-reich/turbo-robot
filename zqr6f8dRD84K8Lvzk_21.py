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

def hex(x):
  return 1+3*x*(x-1)
​
def hex_lattice(n):
  c=int(((n-1)/3)**.5+1)
  if n!=hex(c): return "Invalid"
  l=r=' o'*(2*c-1) + ' '
  for i in reversed(range(c-1)):
    l=' '+l[:len(l)//2-1]+l[len(l)//2+1:]+' '
    r=l+'\n'+r+'\n'+l
  return r

