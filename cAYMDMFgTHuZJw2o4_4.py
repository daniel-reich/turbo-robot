"""


Suppose an image can be represented as a 2D list of 0s and 1s. Create a
function to reverse an image. Replace the 0s with 1s and vice versa.

### Examples

    reverse_image([
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]
    ]) ➞ [
      [0, 1, 1],
      [1, 0, 1],
      [1, 1, 0]
    ]
    
    reverse_image([
      [1, 1, 1],
      [0, 0, 0]
    ]) ➞ [
      [0, 0, 0],
      [1, 1, 1]
    ]
    
    reverse_image([
      [1, 0, 0],
      [1, 0, 0]
    ]) ➞ [
      [0, 1, 1],
      [0, 1, 1]
    ]

### Notes

N/A

"""

def reverse_image(image):
  return [[1 if j == 0 else 0 for j in i]for i in image]

