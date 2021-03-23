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
  
  Sample = image
  
  Negative = []
  
  Counter = 0
  Length = len(image)
  
  while (Counter < Length):
  
    Batch = []
    Item = Sample[Counter]
    
    Cursor = 0
    Span = len(Item)
    
    while (Cursor < Span):
      
      Thing = Sample[Counter][Cursor]
      
      if (Thing == 0):
        Batch.append(1)
        Cursor += 1
      elif (Thing == 1):
        Batch.append(0)
        Cursor += 1
      else:
        Cursor += 1
      
    Negative.append(Batch)
    Counter += 1
  
  return Negative

