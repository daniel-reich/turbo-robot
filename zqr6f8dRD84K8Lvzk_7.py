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
    lattices = [0,1]
    index = 1
    while lattices[-1] < n:
        lattices.append(lattices[-1]+6*index)
        index+=1
    if n not in lattices: return "Invalid"
    returnLattice = ""
    minOs = lattices.index(n)
    maxOs = minOs*2-1
    rowLength = maxOs*2+1
    row = 1
    midRow = maxOs/2 + 0.5
    while row <= maxOs:
        if row < maxOs/2:
            numOs = minOs + row - 1 
        elif row > maxOs/2:
            numOs = maxOs - (row-midRow)
        else:
            numOs = maxOs
        
        
        Oindex = 0
        Ostring = " "
        while Oindex < numOs:
            Ostring += "o "
            Oindex  += 1
            
        
        if len(Ostring) < rowLength:
            spaces = ""
            spaceCount = int((rowLength - len(Ostring))/2)
            for each in range(0, spaceCount):
                spaces+=" "
            Ostring = spaces + Ostring + spaces
        
        if row != maxOs:
            Ostring += "\n"
        
        returnLattice += Ostring
            
        row+=1   
    
    return returnLattice

