"""


Create a function that determines whether elements in an array can be re-
arranged to form a consecutive list of numbers where **each number appears
exactly once**.

### Examples

    cons([5, 1, 4, 3, 2]) ➞ True
    // Can be re-arranged to form [1, 2, 3, 4, 5]
    
    cons([5, 1, 4, 3, 2, 8]) ➞ False
    
    cons([5, 6, 7, 8, 9, 9]) ➞ False
    // 9 appears twice

### Notes

N/A

"""

def cons(lst):
  lst = sorted(lst)
  count = {}
​
  for f in lst:
    count[f] = lst.count(f)
​
  if 2 in count.values():
    return False
  
    
  smallest = lst[0]
  biggest  = lst[0]
  for num in lst:
    if num > biggest:
      biggest = num
    elif num < smallest:
      smallest = num
  l_st = [x for x in range(smallest , biggest+1)]
  print(lst , l_st)
  for index in range(len(l_st)):
    if l_st[index] != lst[index]:
      return False
  return True

