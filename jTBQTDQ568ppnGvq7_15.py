"""


Write a function that sorts a list of integers by their digit length in
**descending order** , then settles ties by sorting numbers with the same
digit length in **ascending order**.

### Examples

    digit_sort([77, 23, 5, 7, 101])
    ➞ [101, 23, 77, 5, 7]
    
    digit_sort([1, 5, 9, 2, 789, 563, 444])
    ➞ [444, 563, 789, 1, 2, 5, 9]
    
    digit_sort([53219, 3772, 564, 32, 1])
    ➞ [53219, 3772, 564, 32, 1]

### Notes

N/A

"""

import operator
def digit_sort(lst):
    temp = []
    for i in range(len(lst)):
        temp.append([lst[i],len(str(lst[i]))])
​
    temp = sorted(temp, key = operator.itemgetter(0))
    temp = sorted(temp, key = operator.itemgetter(1),reverse=True)
    myans = []
    for i in range(len(temp)):
        myans.append(temp[i][0])
​
    return myans

