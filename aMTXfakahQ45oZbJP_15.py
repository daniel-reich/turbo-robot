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

def complete_bracelet(lst):
    seq = "No"
    for i in range(1, len(lst)):
        p1 = lst[0:i+1]
        p2 = lst[i+1:i+3+(i-1)]
        if p1 == p2: 
            lengthtravel = len(p1+p2)
            pattern = p1
            patternlength = len(p1)
            seq = "Yes"
            break
        p1 = []
        p2 = []
    if seq == "No": return False 
    i = lengthtravel
    lst2 = lst[i:].copy()
    while i < len(lst):
        if lst[i:(i+patternlength)] == pattern:
            lst2 = lst2[i+patternlength:]
        i += 1
    if lst2 == []: return True
    return False

