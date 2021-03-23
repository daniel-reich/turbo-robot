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

import math
​
def hex_lattice(n):
    for num in range(n + 1):
        hexagonalVal = 1 + 6*((num*(num-1))/2)
        if hexagonalVal == n:
            break
        elif hexagonalVal > n:
            return "Invalid"
​
    hexagonalRoot = int((3 + math.sqrt(12*n - 3))/6)
    
    height = 2*hexagonalRoot - 1
    rowLen = 4*hexagonalRoot-1
    
    dots = hexagonalRoot
    spaceAmt = hexagonalRoot
    spaceAccom = 0
​
    idx1 = -1
    idx2 = 1
​
    string = ''
​
    i = 0
    while i < height:
        j = 0
        while j < rowLen:
            if j != spaceAmt:
                string += ' '
            else:
                k = 0
                while k < dots:
                    if k != dots - 1:
                        string += 'o '
                    else:
                        string += 'o'
                    k += 1
                j = 3*hexagonalRoot-2 + spaceAccom
                
            j += 1
        
        if i != height - 1:
            string += '\n'
​
        dots += idx2
        spaceAccom += idx2
        spaceAmt += idx1
        if spaceAmt == 1:
            idx1 = 1
            idx2 =- 1
​
        i += 1
​
    return string

