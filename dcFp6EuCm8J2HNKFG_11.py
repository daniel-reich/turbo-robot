"""


Write a function that returns the sum of all the `elements` included in the
`root list`.

### Examples

    func([ [], [] ,[] ]) ➞ 3
    # 1 + 1 + 1 = 3
    # The three empty lists inside the root list.
    
    func([ [3], [2] ,[1,2] ]) ➞ 7
    # 1 + 1 + 1 = 3
    # The three lists inside the root list.
    # 1 + 1 + 2 = 4
    # The elements inside the previous lists.
    # 4 + 3 = 7
    
    func([]) ➞ 0
    # The root list is empty thus there are no elements.
    
    func([[[]]]) ➞ 2
    # 1
    # The only list in the root list.
    # 1
    # The empty list in the previous list.
    # 1 + 1 = 2

### Notes

If a list is empty return/add `0`.

"""

import re 
def func(l):
    return len(re.findall('[0-9A-Za-z]',str(l)))+(str(l).count('[')-1)
