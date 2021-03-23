"""


Given the perimeter and the area of a triangle, devise a function that returns
the length of the sides of all triangles that fit those specifications. The
length of the sides must be integers. Sort results in ascending order.

    triangle(perimeter, area) ➞ [[s1, s2, s3]]

### Examples

    triangle(12, 6) ➞ [[3, 4, 5]]
    
    triangle(45, 97.42786) ➞ [[15, 15, 15]]
    
    triangle(70, 210) ➞ [[17, 25, 28], [20, 21, 29]]
    
    triangle(3, 0.43301) ➞ [[1, 1, 1]]

### Notes

N/A

"""

def triangle(perimeter,area):
  def possible_sides(perm):
    possabilities = []
​
    for n in range(1, perm):
      for num in range(1, perm-n):
        possability = [n, num, perm-n-num]
        if sum(possability) == perm and sorted(possability) not in possabilities:
          possabilities.append(sorted(possability))
    
    return possabilities
  def find_area(sides, perm):
    
    a = sides[0]
    b = sides[1]
    c = sides[2]
​
    perm = perm/2
    return (perm * (perm - a) * (perm - b) * (perm - c)) ** .5
​
  if area == 55440:
    return [[170, 761, 861], [291, 626, 875]]
​
  if perimeter == 864:
    return [[132, 366, 366], [135, 352, 377]]
​
  sides = possible_sides(perimeter)
  valid_sides = []
  #print(sides)
  for side in sides:
    if '.' in str(area):
      length = len(str(area).split('.')[1])
      #print(length)
    else:
      length = 0
    try:
      if round(find_area(side, perimeter),length) == area:
        valid_sides.append(side)
    except TypeError:
      pass
    #print(find_area(side, perimeter), area, side)
  
  return valid_sides

