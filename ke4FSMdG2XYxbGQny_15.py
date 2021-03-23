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
    b=[]
    i=0
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            b.append(lst[i]-(2*n))
        else:
            b.append(lst[i]+(2*n))
    return b

