"""


Write a function that divides a list into chunks of size **n** , where **n**
is the length of each chunk.

### Examples

    chunkify([2, 3, 4, 5], 2) ➞ [[2, 3], [4, 5]]
    
    chunkify([2, 3, 4, 5, 6], 2) ➞ [[2, 3], [4, 5], [6]]
    
    chunkify([2, 3, 4, 5, 6, 7], 3) ➞ [[2, 3, 4], [5, 6, 7]]
    
    chunkify([2, 3, 4, 5, 6, 7], 1) ➞ [[2], [3], [4], [5], [6], [7]]
    
    chunkify([2, 3, 4, 5, 6, 7], 7) ➞ [[2, 3, 4, 5, 6, 7]]

### Notes

  * It's O.K. if the last chunk is not completely filled (see example #2).
  * Integers will always be single-digit.

"""

def chunkify(lst,size):
    j = 0
    b = []
    if len(lst) < size:
        return [lst]
    while j < len(lst) - (len(lst)%size):
        a = []
        
        for i in range(size):
            a.append(lst[i+j])
        j += size 
        b.append(a)
    if len(lst)%size == 0:
        return b 
    else:
        c = []
        for i in range(len(lst)%size):
            c.append(lst[-(i+1)])
        b.append(c)
        return b

