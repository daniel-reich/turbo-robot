"""


Given a shuffled list `l`, return a sequence of _transpositions_ which sorts
the list (as in `sorted(l)`). A transposition is a pair of indices `(i, j)`
representing that `l[i]` and `l[j]` be swapped. Specifically, the output is a
list of transpositions to be applied. Transpositions are applied as in:

    def apply_transpositions(l, swaps):
      for i, j in swaps:
      l[i], l[j] = l[j], l[i]
    return l

### Examples

    sorting_steps([5, -5]) ➞ [(0, 1)]
    # Swap first and second elements.
    
    sorting_steps([4, 3, 2, 1]) ➞ [(0, 3), (1, 2)] or even [(0, 1), (1, 2), (2, 3), (0, 1), (1, 2), (0, 1)]
    
    sorting_steps([6, 6]) ➞ []

### Notes

Output is not unique! A given list may be sorted with varying numbers of
transpositions stemming from various sorting techniques. You need only produce
output which works. (This gives the problem algorithimic freedom!)

"""

from copy import copy
def sorting_steps(lst):
    swaps = []
    if len(lst) == 0 or len(lst) == 1 :
        return []
    print (lst)
    correct = {} 
    for u in set(lst):
        v = [pair[1] for pair in zip(sorted(lst),range(len(lst))) if pair[0] == u]
        correct[u] = v
    print (correct)
    while lst != sorted(lst):
        num = [k for k,v in correct.items() if len(v)>0][0]
        num_pos = lst.index(num)
        num_corr = correct[num].pop()
        print(num, num_pos, num_corr)
        while num_corr != num_pos and lst[num_corr] != num:
            swaps.append([num_corr, num_pos])
            lst[num_corr], lst[num_pos], num = num, lst[num_corr], lst[num_corr]
            print (lst)
            num_pos = lst.index(num)
            if len(correct[num]) == 0:
                break
            num_corr = correct[num].pop()
            print(num, num_pos, num_corr)
    return swaps

