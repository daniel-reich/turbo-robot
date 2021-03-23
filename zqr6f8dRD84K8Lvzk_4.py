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

def hex_lattice(n):
    ans=''
    p=(3+(12*n-3)**.5)/6
    if not p.is_integer():
        return 'Invalid'
    rows=0;ds=-1;dc=1;cc=int(p)-1;sc=int(p)
    while rows<2*int(p)-1:
        ans+=' '*sc+'o '*cc+'o'+' '*sc+'\n'
        sc+=ds
        cc+=dc
        rows+=1
        if sc==1:
            ds=1
            dc=-1
    return ans[:-1]

