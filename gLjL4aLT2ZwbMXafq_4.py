"""


Find all swap pairs between two lists such that the sums of lists after the
swap are equal. The input is two lists of integers, not necessarily of the
same length. The output is a set of tuples `{(num_from_l1, num_from_l2), ..}`.
If there is no pair found return an empty set.

### Examples

    fair_swap([1, 1], [2, 2]) ➞ {(1, 2)}
    
    fair_swap([1, 2], [2, 3]) ➞ {(1, 2), (2, 3)}
    
    fair_swap([2], [1, 3]) ➞ {(2, 3)}
    
    fair_swap([2, 3, 4], [11, 4, 1]) ➞ set()

### Notes

N/A

"""

def fair_swap(l1, l2):
    s, swap = set(), False
    if sum(l1) < sum(l2):
        l1, l2 = l2, l1
        swap = True
    one, two = sum(l1), sum(l2)
    if (one + two) % 2 == 1:
        return s
    dif = one - two
    for i in l1:
        look = i - (dif // 2)
        if look in l2:
            if swap:
                add = (look, i)
            else:
                add = (i, look)
            s.add(add)
    return s

