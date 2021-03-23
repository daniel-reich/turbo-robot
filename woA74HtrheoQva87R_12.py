"""


Create a function that concatenates **n** input lists, where **n** is
variable.

### Examples

    concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]
    
    concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]
    
    concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]
    
    concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]

### Notes

Lists should be concatenated in order of the arguments.

"""

def concat(*args):
    z =''
    for num in args:
      for i in range(0,len(num)):
       z= z+str(num[i])
    return list(float(num) if num.isalpha()==False  else num for num in z  )

