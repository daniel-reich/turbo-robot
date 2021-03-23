"""


Write a function that returns the next number that can be created from the
same digits as the input.

### Examples

    next_number(19) ➞ 91
    
    next_number(3542) ➞ 4235
    
    next_number(5432) ➞ 5432
    
    next_number(58943) ➞ 59348

### Notes

  * If no larger number can be formed, return the number itself.
  *  **Bonus** : See if you can do this without generating all digit permutations.

"""

def next_number(num):
  arr = [int(x) for x in str(num)]
  i = len(arr) - 1
  while i > 0 and arr[i - 1] >= arr[i]:
    i -= 1
  if i <= 0:
    return num
  j = len(arr) - 1
  while arr[j] <= arr[i - 1]:
    j -= 1
  arr[i - 1], arr[j] = arr[j], arr[i - 1]
  arr[i:] = arr[len(arr) - 1: i - 1: -1]
  return int(''.join([str(r) for r in arr]))

