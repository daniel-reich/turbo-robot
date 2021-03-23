"""


A **complete bracelet** is a list with at least one subsequence (pattern)
repeating _at least two times_ , and _completely_ \- the subsequence cannot be
cut-off at any point. The subsequence **must have length two or greater**.

 **Complete bracelets** :

    [1, 2, 3, 3, 1, 2, 3, 3]  # Pattern: [1, 2, 3, 3]
    
    [1, 2, 1, 2, 1, 2, 1, 2]  # Pattern: [1, 2] or [1, 2, 1, 2]
    
    [1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7]  # Pattern: [1, 1, 6, 1, 1, 7]
    
    [4, 4, 3, 4, 4, 4, 4, 3, 4, 4]  # Pattern: [4, 4, 3, 4, 4]

 **Incomplete bracelets** :

    [1, 2, 2, 2, 1, 2, 2, 2, 1]  # Incomplete (chopped off)
    
    [1, 1, 6, 1, 1, 7]  # Incomplete (subsequence repeats only once)

Create a function that returns `True` if a bracelet is **complete** , and
`False` otherwise.

### Examples

    complete_bracelet([1, 2, 2, 1, 2, 2]) ➞ True
    
    complete_bracelet([5, 1, 2, 2]) ➞ False
    
    complete_bracelet([5, 5, 5]) ➞ False
    # potential pattern [5, 5] cut-off (patterns >= 2)

### Notes

  * Patterns must be at least two integers in length.
  * See **Comments** for a hint if you are stuck.

"""

def complete_bracelet(bracelet):
    '''
    Returns True if bracelet has at least 2 consecutive identical subsequences
    of length at least 2 as per the instructions.
    '''
    size = len(bracelet)
    max_seq  = size // 2  # longest subsequence which could repeat
    seg_size = 2  # size of subsequence being checked for repetition
    ptr = 0  # index to start check from
​
    while seg_size <= max_seq:
        okay = True
        while ptr + seg_size * 2 <= size:
            if bracelet[ptr:ptr+seg_size] != bracelet[ptr+seg_size:ptr+2*seg_size]:
                okay = False
                break # try next biggest size
            ptr += seg_size
            
        if okay and size % seg_size == 0:
            return True   # got to end of bracelet with all repeating
        
        seg_size += 1
        ptr = 0  # try again with bigger subsequence size
​
    return False

