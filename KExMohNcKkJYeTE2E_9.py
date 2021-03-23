"""


Create a function that takes two vectors as lists and checks if the two
vectors are orthogonal or not. The return value is boolean. Two vectors
`first` and `second` are orthogonal if their dot product is equal to zero.

### Examples

    is_orthogonal([1, 2], [2, -1]) ➞ True
    
    is_orthogonal([3, -1], [7, 5]) ➞ False
    
    is_orthogonal([1, 2, 0], [2, -1, 10]) ➞ True

### Notes

  * The two lists are of same length.
  * Check out the **Resource** tab.

"""

def is_orthogonal(first, second):
  result = 0
  for i in range(len(first)):
    result = (first[i]*second[i]) + result
  if result == 0:
    return True
  else:
    return False

