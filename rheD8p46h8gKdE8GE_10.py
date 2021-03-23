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

def grayscale(lst):
  for layer in lst:
    for pixel in layer:
      for i in [0,1,2]:
        if pixel[i] < 0:
          pixel[i] = 0
        if pixel[i] > 255:
          pixel[i] = 255
      grey = round((pixel[0]+pixel[1]+pixel[2])/3)
      pixel[0],pixel[1],pixel[2] = grey,grey,grey
  return lst

