"""


Create a function that takes a list of pyramid numbers and returns the maximum
sum of consecutive numbers from the top to the bottom of the pyramid.

                            /3/
                            \7\ 4 
                           2 \4\ 6 
                          8 5 \9\ 3
    
    # Longest slide down sum is 3 + 7 + 4 + 9 = 23

### Examples

    longest_slide([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) ➞ 23
    
    longest_slide([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) ➞ 20
    
    longest_slide([[2], [9, 4], [1, 8, 7], [6, 4, 7, 2]]) ➞ 26

### Notes

N/A

"""

def merge(a, b):
    int_len = max(len(a), len(b))
    arr_res = []
    
    for idx, item in enumerate(b):
        idx_upper_1 = idx-1 if idx -1 >= 0 else idx 
        idx_upper_2 = idx if idx <= len(a)-1 else idx-1 
        arr_res.append(max(item + a[idx_upper_1], item + a[idx_upper_2]))
    return arr_res
        
​
def longest_slide(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]
    
    temp = merge(pyramid[0], pyramid[1])
    for i in range(2,len(pyramid)):
        temp = merge(temp, pyramid[i])
    return max(temp)

