"""


In this challenge you will be given a list similar to the following:

    [[3], 4, [2], [5], 1, 6]

In words, elements of the list are _either an integer or a list containing a
single integer_. If you try to sort this list via `sorted([[3], 4, [2], [5],
1, 6])`, Python will whine about not being able to compare integers and lists.

However, us humans can clearly see that this list can reasonably be sorted
according to "the content of the elements" as:

    [1, [2], [3], 4, [5], 6]

Create a function that, given a list similar to the above, sorts the list
according to the "content of the elements".

### Examples

    sort_it([4, 1, 3]) ➞ [1, 3, 4]
    
    sort_it([[4], [1], [3]]) ➞ [[1], [3], [4]]
    
    sort_it([4, [1], 3]) ➞ [[1], 3, 4]
    
    sort_it([[4], 1, [3]]) ➞ [1, [3], [4]]
    
    sort_it([[3], 4, [2], [5], 1, 6]) ➞ [1, [2], [3], 4, [5], 6]

### Notes

To reiterate, elements of the list will be either integers or lists with a
single integer.

"""

def sort_it(lst):
    ans = []
    while lst:
        m = lst[0]
        for i in lst:
            var_type = type(i).__name__
            min_type = type(m).__name__
            case1 = var_type == 'list' and min_type == 'list' and i[0] < m[0]
            case2 = var_type == 'list' and min_type == 'int' and i[0] < m
            case3 = var_type == 'int' and min_type == 'list' and i < m[0]
            case4 = var_type == 'int' and min_type == 'int' and i < m
            if (case1) or (case2) or (case3) or (case4):
              m = i
        ans.append(m)
        lst.remove(m)
    return ans

