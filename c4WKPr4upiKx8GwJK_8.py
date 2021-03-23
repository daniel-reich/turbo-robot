"""


Given a list `nums` where each integer is between 1 and 100, return a **sorted
list** containing only **duplicate numbers** from the given `nums` list.

### Examples

    duplicate_nums([1, 2, 3, 4, 3, 5, 6]) ➞ [3]
    
    duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]) ➞ [72, 81, 99]
    
    duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ None

### Notes

The given list won't contain the same number three times.

If there are no duplicate numbers, return None.

"""

def tri_insertion(list):
    for j in range(1, len(list)):
        cle = list[j]
        i = j - 1
        while i >= 0 and list[i] > cle:
            list[i + 1] = list[i]
            i = i - 1
        list[i + 1] = cle
​
def duplicate_nums(nums):
    _size = len(nums) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if nums[i] == nums[j] and nums[i] not in repeated: 
                repeated.append(nums[i]) 
    if not repeated == []:
        tri_insertion(repeated)
        return repeated

