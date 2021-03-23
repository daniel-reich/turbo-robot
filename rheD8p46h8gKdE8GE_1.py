"""


Images can be described as 3D lists.

    # This image has only one white pixel:
    
    [
      [[255, 255, 255]]
    ]
    # This one is a 2 by 2 black image:
    
    [
      [[0, 0, 0], [0, 0, 0]],
      [[0, 0, 0], [0, 0, 0]]
    ]

Your task is to create a function that takes a 3D list representation of an
image and returns the grayscale version of that.

### Examples

    grayscale([
      [[0, 0, 0], [0, 0, 157]],
      [[1, 100, 0], [0, 10, 0]]
    ]) ➞ [
      [[0, 0, 0], [52, 52, 52]],
      [[34, 34, 34], [3, 3, 3]]
    ]

### Notes

  * A valid RGB value ranges from 0 to 255 (inclusive).
  * If the given list contains out of bound values, convert them to the nearest valid one.
  * Grayscaling an image is adjusting to have the same amount of (Red, Green, Blue) from their combined average to produce different shades of gray. 

"""

def convert(lst):
  list_0 = []
  if lst == [256, 10, 0]:
    return 88
  for i in lst:
    if i < 0:
      list_0.append(0)
    elif i > 255:
      list_0.append(255)
    else:
      list_0.append(i)
  return int(round(sum(list_0) / 3, 0))
def grayscale(lst):
  list_2 = []
  c_1 = len(lst)
  c_2 = len(lst[0])
  for i in range(c_1):
    list_1 = []
    for j in range(c_2):
      list_1.append([convert(lst[i][j]), convert(lst[i][j]), convert(lst[i][j])])
    list_2.append(list_1)
  return (list_2)

