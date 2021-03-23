"""


Create a function that groups a list of numbers based on a **size** parameter.
The **size** represents the maximum length of each sub-list.

    [1, 2, 3, 4, 5, 6], 3
    [[1, 3, 5], [2, 4, 6]]
    # Divide list into groups of size 3.
    
    [1, 2, 3, 4, 5, 6], 2
    [[1, 4], [2, 5], [3, 6]]
    # Divide list into groups of size 2.
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4
    [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9]]
    # "Leftover" lists are okay.

### Examples

    group([1, 2, 3, 4], 2) ➞ [[1, 3], [2, 4]]
    
    group([1, 2, 3, 4, 5, 6, 7], 4) ➞ [[1, 3, 5, 7], [2, 4, 6]]
    
    group([1, 2, 3, 4, 5], 1) ➞ [[1], [2], [3], [4], [5]]
    
    group([1, 2, 3, 4, 5, 6], 4) ➞ [[1, 3, 5], [2, 4, 6]]

### Notes

  * The **size** parameter represents the maximum size for each sub-list (see ex.4). You should try to fill each sub-list evenly. In other words, ex.4 should be `[[1, 3, 5], [2, 4, 6]]`, not `[[1, 3, 5, 6], [2, 4]]`.
  * Keep the relative order of the numbers in each sub-list the same as the order in the original list.

"""

def group(lst, size):
    """
    Slice a list into chunks of given size
    or equal size
    """
    from math import ceil
​
    if size < 1: return []
    
    bs = best_size(len(lst), size)
    chunks = ceil(len(lst)/bs)
​
    result = []
    for i in range(chunks):
        sub = []
        for j in range(bs):
            try: sub.append(lst[i+j*chunks])
            except: pass
        result.append(sub)
       
    return result
​
def best_size(lenght:int, max_size:int):
    """
    Find divisor of lenght that is equal
    or lesser than max_size
    """
    for size in  range(max_size, 1, -1):
        if lenght % size == 0:
            return  size
    return max_size

