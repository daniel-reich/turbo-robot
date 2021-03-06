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

def pop(state):
  
  # Checking to see if 'state' are all zeroes
  
  Total = sum(state)
  
  if (Total == 0):
    return state
  
  # Checking to see where non-zero item is
  
  Position = 0
  Counter = 0
  Length = len(state)
  
  while (Counter < Length):
    
    Item = state[Counter]
    
    if (Item == 0):
      Counter += 1
    else:
      Position = Counter
      Counter += 1
  
  # Amending Values 
  
  Cursor_A = Position - 1
  Cursor_B = Position + 1
  Value = state[Position] - 1
  Length = len(state)
  
  while (Value > 0):
    
    if (Cursor_A >= 0) and (Cursor_B < Length):
      state[Cursor_A] = Value
      state[Cursor_B] = Value
      Value -= 1
      Cursor_A -= 1
      Cursor_B += 1
  
    elif (Cursor_A >= 0) and (Cursor_B >= Length):
      state[Cursor_A] = Value
      Value -= 1
      Cursor_A -= 1
  
    elif (Cursor_A < 0) and (Cursor_B < Length):
      state[Cursor_B] = Value
      Value -= 1
      Cursor_B += 1
  
    else:
      Cursor_A -= 1
      Cursor_B += 1
  
  # Giving Answer
  return state

