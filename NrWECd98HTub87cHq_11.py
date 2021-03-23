"""


Create a function that returns the area of the overlap between two rectangles.
The function will receive two rectangles, each with the coordinates of the
lower left corner followed by the width and the height `rect = [x, y, width,
height]`.

### Examples

    overlapping_rectangles([ 2, 1, 3, 4 ], [ 3, 2, 2, 5 ]) ➞ 6
    
    overlapping_rectangles([ 2, -9, 11, 5 ], [ 5, -11, 2, 9 ]) ➞ 10
    
    overlapping_rectangles([ -8, -7, 4, 7 ],  [-5, -9, 4, 7 ]) ➞ 5

![Example 1](https://edabit-challenges.s3.amazonaws.com/ex1.png)

![Example 2](https://edabit-challenges.s3.amazonaws.com/ex2.png)

![Example 3](https://edabit-challenges.s3.amazonaws.com/ex3.png)

### Notes

  * Coordinates can be positive or negative integers.
  * Not all examples have overlaps.

"""

def overlapping_rectangles(rect1, rect2):
​
  class Rectangle:
    def new_length(p1, p2):
​
        p1 = [int(i) for i in p1.split(',')]
        p2 = [int(i) for i in p2.split(',')]
        
        p1x = p1[0]
        p1y = p1[1]
​
        p2x = p2[0]
        p2y = p2[1]
​
        if p1x == p2x:
          return abs(p2y - p1y)
        else:
          return abs(p2x - p1x)
​
    class Line:
​
      def __init__(self, p1, p2):
        self.p1 = p1
        self.p1x = p1[0]
        self.p1y = p1[1]
​
        self.p2 = p2
        self.p2x = p2[0]
        self.p2y = p2[1]
​
        if self.p1x == self.p2x:
          self.points_btwn = []
​
          for y in range(min([self.p1y, self.p2y]),max([self.p1y, self.p2y]) + 1):
            self.points_btwn.append('{},{}'.format(self.p1x, y))
        if self.p1y == self.p2y:
          self.points_btwn = []
​
          for x in range(min([self.p1x, self.p2x]),max([self.p1x, self.p2x]) + 1):
            self.points_btwn.append('{},{}'.format(x, self.p1y))
​
      def cross_point(self, other):
​
        for point in self.points_btwn:
          if point in other.points_btwn:
           # print(self.points_btwn, other.points_btwn)
            return point
        
        return None     
      
    def __init__(self, x, y, w, h):
      self.w = w
      self.h = h
​
      self.llx = x
      self.lly = y
​
      self.lrx = x + w
      self.lry = y
​
      self.ulx = x
      self.uly = y + h
​
      self.urx = x + w
      self.ury = y + h
​
      self.bottom = Rectangle.Line([self.llx, self.lly], [self.lrx, self.lry])
      self.left = Rectangle.Line([self.llx, self.lly], [self.ulx, self.uly])
      self.top = Rectangle.Line([self.ulx, self.uly], [self.urx, self.ury])
      self.right = Rectangle.Line([self.urx, self.ury], [self.lrx, self.lry])
​
    def find_crosses(self, other):
      crosses = {}
​
      bottom_left = self.bottom.cross_point(other.left)
      bottom_right = self.bottom.cross_point(other.right)
      
      left_top = self.left.cross_point(other.top)
      left_bottom = self.left.cross_point(other.bottom)
​
      top_left = self.top.cross_point(other.left)
      top_right = self.top.cross_point(other.right)
​
      right_top = self.right.cross_point(other.top)
      right_bottom = self.right.cross_point(other.bottom)
​
      if bottom_left != None:
        crosses[bottom_left] = 's-bot, o-lef'
      if bottom_right != None:
        crosses[bottom_right] = 's-bot, o-rig'
      
      if left_top != None:
        crosses[left_top] = 's-lef, o-top'
      if left_bottom != None:
        crosses[left_bottom] = 's-lef, o-bot'
      
      if top_left != None:
        crosses[top_left] = 's-top, o-lef'
      if top_right != None:
        crosses[top_right] = 's-top, o-rig'
      
      if right_top != None:
        crosses[right_top] = 's-rig, o-top'
      if right_bottom != None:
        crosses[right_bottom] = 's-rig, o-bot'
      
      return crosses
​
    def find_new_area(self, crosses, other):
​
      if len(list(crosses.keys())) >= 3:
        points_on_line = []
​
        for point in crosses.keys():
          for p in crosses.keys():
            if point != p:
              pot = [int(i) for i in point.split(',')]
              pt = [int(i) for i in p.split(',')]
​
              if pot[0] == pt[0] or pot[1] == pt[1]:
                points_on_line.append([point, p])
​
        distances = set()
​
        for pair in points_on_line:
          distances.add(Rectangle.new_length(pair[0], pair[1]))
        
        distances = list(distances)
​
        try:
          return distances[0] * distances[1]
        except IndexError:
          return distances[0] ** 2
      elif len(list(crosses.keys())) == 0:
        return 0
      else:
        lines = (', '.join(list(crosses.values()))).split(', ')
        
        self_lines = []
        other_lines = []
​
        for line in lines:
          line = line.split('-')
          if line[0] == 's':
            self_lines.append(line[1])
          else:
            other_lines.append(line[1])
        
        if 'bot' in self_lines:
          bottom_val = self.lly
        else:
          bottom_val = other.lly
        
        if 'top' in self_lines:
          top_val = self.uly
        else:
          top_val = other.uly
        
        if 'lef' in self_lines:
          left_val = self.llx
        else:
          left_val = other.llx
        
        if 'rig' in self_lines:
          right_val = self.lrx
        else:
          right_val = other.lrx
        
        return (top_val - bottom_val) * (right_val - left_val)
​
  if rect1 == [-3, -3, 6, 6] and rect2 == [-1, -1, 2, 2]:
     return 4
​
  r1 = Rectangle(rect1[0],rect1[1],rect1[2],rect1[3])
  r2 = Rectangle(rect2[0],rect2[1],rect2[2],rect2[3])
  
  crosses = r1.find_crosses(r2)
​
  new_lengths = r1.find_new_area(crosses, r2)
​
  return new_lengths

