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
    return sorted(lst, key=get_key)
​
def get_key(x):
    if type(x) == list:
        return x[0]
    return x

