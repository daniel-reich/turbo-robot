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
    greyscale = []
    for a in range(0,len(lst)):
        layer = []
        for row in range(0,len(lst[a])):
            for i in range(0,len(lst[a][row])):
                if lst[a][row][i] > 255:
                    lst[a][row][i] = 255
            if sum(lst[a][row]) < 0:
                layer.append([0,0,0])
            else:
                layer.append([round(sum(lst[a][row])/3),round(sum(lst[a][row])/3),round(sum(lst[a][row])/3)])
        greyscale.append(layer)
    return greyscale

