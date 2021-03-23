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

class Colour_triangle:
  class Colour:
​
    def __init__(self, colour):
      self.c = colour
    
    def reproduce(self, other):
      if self.c == other.c:
        return Colour_triangle.Colour(self.c)
      else:
        if sorted([self.c, other.c]) == sorted(['R', 'G']):
          return Colour_triangle.Colour('B')
        elif sorted([self.c, other.c]) == sorted(['R', 'B']):
          return Colour_triangle.Colour('G')
        else:
          return Colour_triangle.Colour('R')
  
  def __init__(self, rawstart):
    
    self.raw = rawstart
​
    firstline = [Colour_triangle.Colour(colour) for colour in self.raw]
​
    self.triangle = {1: firstline}
​
    while min([len(i) for i in self.triangle.values()]) > 1:
      new_line = []
      new_line_ident = max(self.triangle.keys()) + 1
​
    #  print(new_line_ident)
​
      for n in range(len(self.triangle[max(self.triangle.keys())]) - 1):
        c1 = self.triangle[max(self.triangle.keys())][n]
        c2 = self.triangle[max(self.triangle.keys())][n+1]
​
        new_line.append(c1.reproduce(c2))
      
      self.triangle[new_line_ident] = new_line
​
​
def coloured_triangle(row):
​
  CT = Colour_triangle(row)
​
  return CT.triangle[max(CT.triangle.keys())][0].c
