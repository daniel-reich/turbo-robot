"""


Given a list of **even** length, copy the half with the higher sum of numbers
to the other half of the list. If the sum of the first half equals the sum of
the second half, return the original list.

### Examples

    balanced([1, 2, 4, 6, 3, 1]) ➞ [6, 3, 1, 6, 3, 1]
    # 1 + 2 + 4 < 6 + 3 + 1 sol = [6, 3, 1, 6, 3, 1]
    
    balanced([88, 3, 27, 5, 9, 0, 13, 10]) ➞ [88, 3, 27, 5, 88, 3, 27, 5]
    # 88 + 3 + 27 + 5 > 9 + 0 + 13 + 10  sol = [88, 3 ,27 ,5 ,88 ,3 ,27 ,5]
    
    balanced([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]) ➞ [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
    # 7 + 5 + 2 + 6 + 1 + 0 = 1 + 5 + 2 + 7 + 0 + 6 sol =  [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]

### Notes

The length of the list is **even**.

"""

def balanced(lst):
  a = 0
  b = 0
  c = []
  num = int(len(lst)/2)
  for i in range(num):
    a += lst[i]
    b += lst[num+i]
  for i in range(num):
    if a >= b:
      c.append(lst[i])
    else:
      c.append(lst[num+i])
  for i in range(num):
    if a > b:
      c.append(lst[i])
    else:
      c.append(lst[num+i])
  return c

