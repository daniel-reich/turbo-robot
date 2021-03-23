"""


Say you want to traverse a list of integers starting at the first item and
using each value as a pointer of what item to visit next. For example, you
would traverse the list `[1, 4, 3, 0, 2]` in the following manner:

![List](https://edabit-challenges.s3.amazonaws.com/gAbF8Rs.png)

Because you visit every item once and go back to the starting point, the list
`[1, 4, 3, 0, 2]` is a "full cycle".

Create a function that returns `True` if the input list is a full cycle, or
`False` otherwise.

### Examples

    full_cycle([1, 4, 3, 0, 2]) ➞ True
    
    full_cycle([1, 4, 0, 3, 2]) ➞ False
    
    full_cycle([5, 3, 4, 2, 0, 1]) ➞ True

### Notes

Test lists won't include any negative integers.

"""

def full_cycle(lst):
  travel = lambda lst, i: lst[i] if i < len(lst) else False
  used = []
  c = 0
  i = 0
  print(lst)
  while len(set(used)) == len(used) < len(lst) and c < 1000:
    used.append(i)
    i = travel(lst, i)
    print(i, used)
    if i == False:
      return len(set(used)) == len(lst) if max(used) < len(lst) else False
    c += 1
  
  return len(set(used)) == len(lst)

