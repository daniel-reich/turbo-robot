"""


When two blocks of the same "type" are adjacent to each other, the entire
contiguous block disappears (pops off). If this occurs, this can allow
previously separated blocks to be in contact with each other, setting off a
chain reaction. This will continue until each block is surrounded by a
different block.

Here's a demonstration:

    ["A", "B", "C", "C", "B", "D", "A"]
    # The two adjacent Cs pop off
    
    ["A", "B", "B", "D", "A"]
    # Two adjacent Bs pop off
    
    ["A", "D", "A"]
    # No more blocks can be popped off

Another demonstration:

    ["A", "B", "A", "A", "A", "B", "B"]
    # The three adjacent As will pop off
    # (before the two adjacent Bs)
    
    ["A", "B", "B", "B"]
    # 3 adjacent Bs pop off
    
    ["A"]
    # Final result

### Examples

    final_result(["B", "B", "A", "C", "A", "A", "C"]) ➞ ["A"]
    
    final_result(["B", "B", "C", "C", "A", "A", "A"]) ➞ []
    
    final_result(["C", "A", "C"]) ➞ ["C", "A", "C"]

### Notes

If the first round has multiple poppable blocks, pop starting from the left.

"""

def final_result(lst):
  output_lst = []
  
  b = True
  while b:
    i = 0
    indexes_to_delete = []
    prev_item = ""
    next_item = ""
    current_item = ""
    for item in lst:
      if (i == 0 and len(lst) > 1):
        current_item = lst[i]
        next_item = lst[i+1]
        prev_item = ""
      elif (i > 0 and i < len(lst) - 1):
        current_item = lst[i]
        prev_item = lst[i-1]
        next_item = lst[i+1]
      elif (len(lst) > 1):
        current_item = lst[i]
        prev_item = lst[i-1]
        next_item = ""
​
      if (current_item == prev_item and len(lst) > 1):
        if (i not in indexes_to_delete):
          indexes_to_delete.append(i)
        if (i-1 not in indexes_to_delete):
          indexes_to_delete.append(i-1)
      elif (current_item != prev_item and len(indexes_to_delete) > 0):
        break
      i = i + 1
​
    list1 = []
    if (len(indexes_to_delete) > 0):
      for i in range(len(lst)):
        if (i not in indexes_to_delete): 
          list1.append(lst[i])
      lst = list1
      b = True
    else:
      b = False
  
  return lst

