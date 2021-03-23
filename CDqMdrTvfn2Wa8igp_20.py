"""


Create a function that returns the next element in an **arithmetic sequence**.
In an arithmetic sequence, each element is formed by adding the same constant
to the previous element.

### Examples

    next_element([3, 5, 7, 9]) ➞ 11
    
    next_element([-5, -6, -7]) ➞ -8
    
    next_element([2, 2, 2, 2, 2]) ➞ 2

### Notes

All input arrays will contain **integers only**.

"""

def next_element(lst):
    lengthList = len(lst)
    return formula(lst, lengthList)
    
def formula(lst,numTerms):
    firstTerm = lst[0]
    Difference = lst[1]-lst[0]
    nextTermIndex = numTerms + 1
    x_index = firstTerm + Difference*(nextTermIndex-1)
    return x_index

