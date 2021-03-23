"""


A coloured triangle is created from different rows of colours (Red, Green or
Blue). Successive rows, each containing one fewer colour than the last, are
generated by considering the two touching colours in the previous row. If
these colours are identical, the same colour is used in the new row. If
colours are different, the missing colour is used in the new row. This process
continues untill a single colour is generated in the final row.

Different possibilities of colours are:

    Colours Touching:        G G        B G        R G        B R
    New colour:               G          R          B          G

With a bigger example:

    R R G B R G B B
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G

### Goal

  * Create a function which takes **first row** of the triangle as an input and returns the **final colour** which would appear at the bottom row. In above example, given input "RRGBRGBB" will return "G".
  * If you are only given one colour as the input, return that colour.
  * There will be no exception handling case.

### Examples

    coloured_triangle("B") ➞ "B"
    
    coloured_triangle("GB") ➞ "R"
    
    coloured_triangle("RBRGBRB") ➞ "G"

### Notes

N/A

"""

def coloured_triangle(row):
  d = {'BG':'R', 'GR':'B', 'BR':'G', 'G':'G', 'R':'R','B':'B'}
  
  while len(row)>1:
    row = ''.join(d[''.join(sorted(set(row[i:i+2])))] for i in range(len(row)-1))
  return row[0]

