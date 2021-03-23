"""


Create a function that performs an **even-odd** transform to a list, **n
times**. Each **even-odd** transformation:

  1. Adds two ( **+2** ) to each **odd** integer.
  2. Subtracts two ( **-2** ) to each **even** integer.

### Examples

    even_odd_transform([3, 4, 9], 3) ➞ [9, -2, 15]
    # Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]
    
    even_odd_transform([0, 0, 0], 10) ➞ [-20, -20, -20]
    
    even_odd_transform([1, 2, 3], 1) ➞ [3, 0, 5]

### Notes

N/A

"""

def even_odd_transform(lst, n):
  return_list = lst
  for i in range(n):
    for index, number in enumerate(lst):
      if number % 2 == 0:
        return_list[index] = number - 2
      else:
        return_list[index] = number + 2
  return return_list
