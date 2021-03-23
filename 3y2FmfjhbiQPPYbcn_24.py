"""


Once a water balloon pops, is soaks the area around it. The ground gets drier
the further away you travel from the balloon.

The effect of a water balloon popping can be modeled using a list. Create a
function that takes a list which takes the **pre-pop** state and returns the
state after the balloon is popped. The **pre-pop** state will contain **at
most** a single balloon, whose size is represented by the only non-zero
element.

### Examples

    pop([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
    
    pop([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]
    
    pop([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]
    
    pop([0]) ➞ [0]

### Notes

  * Length of input list is always odd.
  * The input list will always be the exact length it takes for there to be exactly one border zero.
  * If the input list consists only of zeroes, return the same list.

"""

def pop(s):
  for i in range(len(s)//2):s[i]=s[-i-1]=i
  return s

