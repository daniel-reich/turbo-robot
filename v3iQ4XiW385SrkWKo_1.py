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
    s=[]
    i=0
    j=0
    a=0
    while i<len(lst):
        if len(s)==0:
            a=lst[i]
            s.append(lst[i])
            j=1
            i+=1
        elif a==lst[i]:
            j=2
            i+=1
        elif a!=lst[i] and j==2:
            s.pop()
            if len(s)==0:
                s.append(lst[i])
                j=1
                a=lst[i]
                i+=1
            else :
                a=s[-1]
                j=1
        elif a!=lst[i] and j==1 :
            a=lst[i]
            s.append(lst[i])
            i+=1
        if i==len(lst) and j==2:
            s.pop()
    return s

