"""


Given three groups of numbers, return a list containing all numbers that
appear in more than one group (in ascending order).

### Examples

    number_groups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5]) ➞ []
    
    number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]) ➞ [1, 3]
    
    number_groups([4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2]) ➞ [2, 4, 9]
    
    number_groups([7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6]) ➞ [5, 8]

### Notes

N/A

"""

def number_groups(group1, group2, group3):
    arr = []
    group1 = [str(i) for i in group1]
    group2 = [str(i) for i in group2]
    group3 = [str(i) for i in group3]
    for i in range(len(group1)):
        if group1[i] in group2 or group1[i] in group3:
            arr.append(group1[i])
        if group2[i] in group3:
            arr.append(group2[i])
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    answer = [int(i) for i in answer]
    answer.sort()
​
    return answer

