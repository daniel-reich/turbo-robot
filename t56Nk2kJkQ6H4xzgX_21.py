"""


Write a function that swaps the X and Y coordinates in a string.

### Examples

    swap_xy("(1, 2), (3, 4)") ➞ "(2, 1), (4, 3)"
    
    swap_xy("(11, 23), (43, 99)") ➞ "(23, 11), (99, 43)"
    
    swap_xy("(-5, -3), (7, 4)") ➞ "(-3, -5), (4, 7)"

### Notes

  * Some numbers have multiple digits.
  * Some numbers will be negative.

"""

def swap_xy(txt):
  lparen1 = txt.find('(')
  comma1 = txt.find(',',lparen1)
  rparen1 = txt.find(')')
  x1 = txt[lparen1+1:comma1]
  y1 = txt[comma1+2:rparen1]
  tuple1 = '('+y1+', '+x1+')'
  lparen2 = txt.rfind('(')
  comma2 = txt.find(',',lparen2)
  x2 = txt[lparen2+1:comma2]
  y2 = txt[comma2+2:-1]
  tuple2 = '('+y2+', '+x2+')'
  return tuple1 + ', ' + tuple2

