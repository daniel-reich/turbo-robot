"""


Create a function that takes an integer and outputs an `n x n` square solely
consisting of the integer `n`.

### Examples

    square_patch(3) ➞ [
      [3, 3, 3],
      [3, 3, 3],
      [3, 3, 3]
    ]
    
    square_patch(5) ➞ [
      [5, 5, 5, 5, 5],
      [5, 5, 5, 5, 5],
      [5, 5, 5, 5, 5],
      [5, 5, 5, 5, 5],
      [5, 5, 5, 5, 5]
    ]
    
    square_patch(1) ➞ [
      [1]
    ]
    
    square_patch(0) ➞ []

### Notes

  * `n >= 0`.
  * If `n == 0`, return an empty list.

"""

def square_patch(n1):
    list1=[[n1]*n1 for j in range(n1)]
    return(list1)

