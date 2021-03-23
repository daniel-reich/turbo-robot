"""


Create a function that counts the number of blocks of **two or more** adjacent
`1`s in a list.

### Examples

    count_ones([1, 0, 0, 1, 1, 0, 1, 1, 1]) ➞ 2
    # Two instances: [1, 1] (middle) and [1, 1, 1] (end)
    
    count_ones([1, 0, 1, 0, 1, 0, 1, 0]) ➞ 0
    
    count_ones([1, 1, 1, 1, 0, 0, 0, 0]) ➞ 1
    
    count_ones([0, 0, 0]) ➞ 0

### Notes

  * A single 1 by itself (surrounded by a zero on its left and right), does **not** count towards the total (see first example).
  * Each input will contain only zeroes and ones.

"""

import re
def count_ones(lst):
    my_str = ""
    for i in range (0,len(lst)):
        my_str+=str(lst[i])
    #print(my_str)
    x = re.split('0',my_str)
    #print(x)
    count = 0
    string = ""
    for i in range (0,len(x)):
        string = x[i]
        if (len(string)>1):
            count+=1
    return count
​
print(count_ones([1, 0, 1, 0, 1, 0, 1, 0]))

