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
    string = ''.join(list(map(str, lst)))
    patterns = [''.join(list(map(str, lst))[:x]) for x in range(1, int(len(lst)/2+1))]
    for i in range(1,int(len(lst)/2)):
        if patterns[i]*int(len(lst)/len(patterns[i])) == string:
            return True
        else: 
            continue
    return False

