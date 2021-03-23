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
​
  poppable = True
​
  while poppable == True and lst != []:
    sn = None
    en = None
​
​
    for n in range(0, len(lst)):
    
      item = lst[n]
​
      try:
        nitem = lst[n + 1]
      except IndexError:
        poppable = False
​
      popped = False
      
      if poppable == True:
        if item == nitem:
          sn = n
​
          for num in range(n, len(lst)):
            
            titem = lst[num]
            if titem != item:
              en = num
              popped = True
              break 
          if popped == False and sn != None:
            en = len(lst)
            popped = True
        if popped == True:
          break
      
    try:
      for n in reversed(range(sn, en)):
        lst.pop(n)
    except TypeError:
      continue
    
  return lst

