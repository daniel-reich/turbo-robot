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
  chars = [",","(", ")"]
  for char in chars:
    txt = txt.replace(char,"")
  txt = txt.split(" ")
  num1 = txt[0]
  num2 = txt[1]
  num3 = txt[2]
  num4 = txt[3]
  
  
  
  
  return "({}, {}), ({}, {})".format(num2,num1,num4,num3)

