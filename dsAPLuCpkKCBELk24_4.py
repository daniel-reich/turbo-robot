"""


You have a list of integers, and for each index you want to find the product
of every integer **except the integer at that index**.

Create a function that takes a list of integers and returns a list of the
products.

### Examples

    get_products([1, 7, 3, 4]) ➞ [84, 12, 28, 21]
    
    get_products([1, 7, 3, 4]) ➞ [84, 12, 28, 21]
    
    get_products([1, 2, 3, 0, 5]) ➞ [0, 0, 0, 30, 0]

### Notes

You can't use division, otherwise you might end up dividing by 0 and the
universe would end.

"""

def multiply(arr):
  result = 1
  for x in arr:
    result*=x
  return result 
  
def get_products(lst):
  arr = [] 
  for i in range(0, len(lst)):
    arr.append(lst[:i] + lst[i+1:])
  return [multiply(x) for x in arr]

