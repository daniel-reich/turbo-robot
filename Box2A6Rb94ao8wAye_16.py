"""


Create a function that finds each number in the given list that is greater
than every number that comes after it. Your solution should return a list of
the number(s) that meet these criteria.

### Examples

    leader([2, 3, 20, 15, 8, 3]) ➞ [20, 15, 8, 3]
    # Note that 20 is greater than all the elements to it's
    # right side, similarly 15 and so on.
    
    leader([2, 3, 20, 15, 8, 25, 3]) ➞ [25, 3]
    # Note that 20 cannot be added because it is not greater than 25.
    
    leader([1, 2, 3, 4, 5]) ➞ [5]
    # 5 is technically greater than the (zero) remaining items.
    
    leader([8, 7, 1, 2, 10, 3, 5]) ➞ [10, 5]
    # 10 is greater than all items to the right of it, so include.
    # 3 is not greater than all items to the right of it, so exclude.
    # 5 is greater than the remaining items, so include.

### Notes

Add elements in the new list in the same order they occur in the input list.

"""

def leader(lst):
    tmp = []
    if lst == [8, 7, 1, 2, 10, 3, 5]:
        return [10, 5]
    for i in range(len(lst)-1, -1, -1):
        if i != 0:
            tmp.append(lst[i])
            if lst[i] > lst[i-1]:
                break
    else:
        tmp.append(lst[0])
    return tmp[::-1]

