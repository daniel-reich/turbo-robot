"""
Given a list of four points in the plane, determine if they are the vertices
of a parallelogram.

### Examples

    is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]) ➞ True
    
    is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]) ➞ False
    
    is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]) ➞ True

### Notes

The points may be given in any order (compare examples #1 and #5).

"""

def is_parallelogram(lst):
​
  class Shape:
    class Point:
      def __init__(self, x, y):
        self.x = x
        self.y = y
          
    class Line:
      def __init__(self, p1, p2):
        
        self.p1 = p1
        self.p2 = p2
​
        self.p1x = p1[0]
        self.p1y = p1[1]
​
        self.p2x = p2[0]
        self.p2y = p2[1]
​
        self.length = ((self.p2x - self.p1x) ** 2 + (self.p2y - self.p1y) ** 2) ** .5
    
    def __init__(self, A, B, C, D):
​
      self.A = Shape.Point(A[0], A[1])
      self.B = Shape.Point(B[0], B[1])
      self.C = Shape.Point(C[0], C[1])
      self.D = Shape.Point(D[0], D[1])
​
      self.AB = Shape.Line(A, B)
      self.BC = Shape.Line(B, C)
      self.CD = Shape.Line(C, D)
      self.DA = Shape.Line(D, A)
​
      if self.AB.length == self.CD.length and self.BC.length == self.DA.length:
        self.is_parallelogram = True
      else:
        self.is_parallelogram = False
  
  from itertools import permutations as p
  permutations = list(p([0, 1, 2, 3], 4))
  
  all_possabilities = []
​
  for permutation in permutations:
    possability = []
    for index in permutation:
      possability.append(lst[index])
    all_possabilities.append(possability)
  
  shapes = []
​
  for possability in all_possabilities:
    A = possability[0]
    B = possability[1]
    C = possability[2]
    D = possability[3]
​
    shapes.append(Shape(A, B, C, D))
  
  for shape in shapes:
    if shape.is_parallelogram == True:
      return True
  
  return False

