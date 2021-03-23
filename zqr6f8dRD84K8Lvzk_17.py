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

def make_hex_list(n):
    res, i = [1], 0
    while res[-1] < n:
        i += 1
        res.append(3 * i * (i + 1) + 1)
    return res
​
​
n_max = 7777
hex_lst = make_hex_list(n_max)
​
​
def hex_lattice(n):
    if n not in hex_lst:
        return 'Invalid'
    idx = hex_lst.index(n)
    res = ' ' + ' '.join('o' for _ in range(2 * idx + 1)) + ' \n'
    for i in range(1, idx + 1):
        line = (' ' + ' ' * i + ' '.join('o' for _ in range(2 * idx + 1 - i))
                + ' ' * i + ' \n')
        res = line + res + line
    return res[:-1]

