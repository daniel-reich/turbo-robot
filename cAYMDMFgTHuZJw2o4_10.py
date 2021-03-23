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

def reverse_image(m):
  return [[1 if i[j]==0else 0 for j in range(len(m[0]))] for i in m]

