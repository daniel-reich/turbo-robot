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
    result = lst
    dropped = ['a']
    while dropped != [] and  len(result) > 1:
        result, dropped = find_dupes(result)
    return result
    
def find_dupes(lst):
    idx = 0
    dropped = []
    while idx < len(lst) - 1 : 
        if lst[idx] == lst [idx + 1]:
            while (idx + 1) < len(lst) and lst[idx] == lst [idx + 1]:            
                dropped.append(lst.pop(idx + 1)) 
            dropped.append(lst.pop(idx))
        idx = idx + 1
    return lst, dropped

