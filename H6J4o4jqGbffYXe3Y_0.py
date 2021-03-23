"""


Write a function which takes a list of numbers and returns a list of tuples
that is a subset of product of the list with itself and first member of each
tuple is less than or equall to the second one.

In mathematical terms:

    A x A = {(x,y)| x∈A and y∈A}
    
    {(x,y)| x>=y, (x,y) ∈ A x A }

### Examples

    relation_list([0, 1, 2, 3]) ➞ [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3)]
    
    relation_lst([858, 544, 164]) ➞ [(164, 164), (164, 544), (164, 858), (544, 544), (544, 858), (858, 858)]
    
    relation_lst([-1]) ➞ [(-1, -1)]
    
    relation_lst([0]) ➞ [(0, 0)]
    
    relation_lst([]), []

### Notes

The result should be in ascending order.

"""

relation_lst=lambda l:sorted(list((y,x)for x in l for y in l if x>=y))

