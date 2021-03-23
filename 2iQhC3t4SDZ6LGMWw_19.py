"""


Given a list of 2D points `[x, y]`, create a function that returns `True` if
those points can be on the _bounds_ of a rectangle, `False` otherwise.

![](https://edabit-challenges.s3.amazonaws.com/fhh2XNW.png)

### Examples

    on_rectangle_bounds([[0, 1], [1, 0], [1, 1], [0, 0]]) ➞ True
    
    on_rectangle_bounds([[0, 1], [1, 0], [1, 1], [0.5, 0.5]]) ➞ False
    
    on_rectangle_bounds([[0, 1], [10, 0], [10, 1]]) ➞ True
    
    on_rectangle_bounds([[0, 1]]) ➞ True

### Notes

Only rectangles with sides parallel to _x-axis_ and _y-axis_ will be
considered.

"""

def sort_count(points, x, y):     # given list of pairs and an x and y value, returns how often those x and y coordinates appeared
  all_x = []
  all_y = []
  for point in points:
    all_x.append(point[0])
    all_y.append(point[1])
  return all_x.count(x), all_y.count(y)
​
​
def on_rectangle_bounds(points):
  if len(points) < 2.5:
    return True
  all_points = points[:]
  most_common_x = sorted(all_points, key = lambda point : sort_count(all_points, point[0], point[1])[0], reverse = True)[0][0]
  most_common_y = sorted(all_points, key = lambda point : sort_count(all_points, point[0], point[1])[1], reverse = True)[0][1]
    
  same_x1 = []
  same_y1 = []
    
  for point in all_points:
    if point[0] == most_common_x:
      same_x1.append(point)
  for p in range(len(all_points)):
    if all_points[p] in same_x1:
      all_points[p] = ['', '']
            
  for point in all_points:
    if point[1] == most_common_y:
      same_y1.append(point)
  for p in range(len(all_points)):
    if all_points[p] in same_y1:
      all_points[p] = ['', ''] 
            
  remaining_points = []
  for point in all_points:
    if point != ['', '']:
      remaining_points.append(point)
    
  same_x2 = []
  same_y2 = []
  second_most_common_x = 0
  second_most_common_y = 0
    
  if remaining_points != []:
    second_most_common_x = sorted(remaining_points, key = lambda point : sort_count(remaining_points, point[0], point[1])[0], reverse=True) [0][0]
    second_most_common_y = sorted(remaining_points, key = lambda point : sort_count(remaining_points, point[0], point[1])[1], reverse=True) [0][1]
    
    for p in range(len(remaining_points)):
      if remaining_points[p][0] == second_most_common_x:
        same_x2.append(remaining_points[p])
    for p in range(len(remaining_points)):
      if remaining_points[p] in same_x2:
        remaining_points[p] = ['','']
            
    for p in range(len(remaining_points)):
      if remaining_points[p][1] == second_most_common_y:
        same_y2.append(remaining_points[p])
    for p in range(len(remaining_points)):
      if remaining_points[p] in same_y2:
        remaining_points[p] = ['','']  
            
  if remaining_points.count(['','']) != len(remaining_points):
    return False    # If there are any points that don't lie on the 4 lines, must be false
   
    # Still need to verify that the 4 lines can form a rectangle
    
    # If above conditions has been met and there are only 2 vertical lines, True
  if same_y1 == [] and same_y2 == []:
    return True
  if (same_y1 == [] or same_y2 == []) and (same_x1 == [] or same_x2 == []):
    return True
    
    # Check that the highest and lowest points on the vertical segments fall between y1 and y2        
  if sorted(same_x1 + same_x2, key = lambda point : point[1]) [0][1] < min(most_common_y, second_most_common_y):
    return False
  if sorted(same_x1 + same_x2, key = lambda point : point[1]) [-1][1] > max(most_common_y, second_most_common_y):
    return False
    
    # Check that the leftmost and rightmost points on the horizontal segments fall between x1 and x2
  if sorted(same_y1 + same_y2, key = lambda point : point[0]) [0][0] < min(most_common_x, second_most_common_x):
    return False
  if sorted(same_y1 + same_y2, key = lambda point : point[0]) [-1][0] > max(most_common_x, second_most_common_x):
    return False   
  return True

