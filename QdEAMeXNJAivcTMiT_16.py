"""


You work in a factory, and your job is to take items from a conveyor belt and
pack them into boxes. Each box can hold a maximum of 10 kgs. Given a list
containing the _weight_ (in kg) of each item, how many boxes would you need to
pack all of the items?

### Example

    boxes([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2]) ➞ 5
    
    # Box 1 = [2, 1, 2, 5] (10kg)
    # Box 2 = [4, 3] (7kg)
    # Box 3 = [6, 1, 1] (8kg)
    # Box 4 = [9] (9kg)
    # Box 5 = [3, 2] (5kg)

### Notes

There will always be a minimum of 1 item to pack. All items will weigh less
than or equal to 10 kgs, and need to be packed in the order that they arrive.

"""

def boxes(weights):
  box_weight = 0
  box_count = 0
  for i in weights:
    if box_weight + i <= 10:
      box_weight += i
    else:
      box_count += 1
      box_weight = i
  box_count += 1
  return box_count

