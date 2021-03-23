"""


Write a function that takes the coordinates of three points in the form of a
2d array and returns the perimeter of the triangle. The given points are the
vertices of a triangle on a two-dimensional plane.

### Examples

    perimeter( [ [15, 7], [5, 22], [11, 1] ] ) ➞ 47.08
    
    perimeter( [ [0, 0], [0, 1], [1, 0] ] ) ➞ 3.42
    
    perimeter( [ [-10, -10], [10, 10 ], [-10, 10] ] ) ➞ 68.28

### Notes

  * The given points always create a triangle.
  * The numbers in the argument array can be positive or negative.
  * Output should have 2 decimal places
  * This challenge is easier than it looks.

"""

def perimeter(lst):
  
  # Working Out Length of Side 1
  
  Side_01_H = abs(lst[0][0] - lst[1][0])
  Side_01_V = abs(lst[0][1] - lst[1][1])
  
  A_Squared = Side_01_H ** 2
  B_Squared = Side_01_V ** 2
  C_Squared = A_Squared + B_Squared
  
  TSL1_Length = C_Squared ** 0.5
  
  # Working Out Length of Side 2
  
  Side_02_H = abs(lst[1][0] - lst[2][0])
  Side_02_V = abs(lst[1][1] - lst[2][1])
  
  A_Squared = Side_02_H ** 2
  B_Squared = Side_02_V ** 2
  C_Squared = A_Squared + B_Squared
  
  TSL2_Length = C_Squared ** 0.5
  
  # Working Out Length of Side 3
  
  Side_03_H = abs(lst[2][0] - lst[0][0])
  Side_03_V = abs(lst[2][1] - lst[0][1])
  
  A_Squared = Side_03_H ** 2
  B_Squared = Side_03_V ** 2
  C_Squared = A_Squared + B_Squared
  
  TSL3_Length = C_Squared ** 0.5
  
  # Working Out Perimeter of Triangle
  Perimeter = TSL1_Length + TSL2_Length + TSL3_Length
  
  # Rounding and Giving Answer
  Answer = round(Perimeter,2)
  return Answer

