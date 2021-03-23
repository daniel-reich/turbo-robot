"""
Create two functions:

  1.  **Leftside function** : Returns count of numbers _strictly smaller_ than `n` on the left.
  2.  **Rightside function** : Returns count of numbers _strictly smaller_ than `n` on the right.

### Examples

    left_side([5, 2, 1, 4, 8, 7]) ➞ [0, 0, 0, 2, 4, 4]
    
    right_side([5, 2, 1, 4, 8, 7]) ➞ [3, 1, 0, 0, 1, 0]
    
    left_side([1, 2, 3, -1]) ➞ [0, 1, 2, 0]
    
    right_side([1, 2, 3, -1]) ➞ [1, 1, 1, 0]

### Notes

"Left" and "right" refer to the number at indices less than or greater than
`n`'s index, respectively.

"""

def left_side(lst):
    result=[]
    for i in range(len(lst)):
        count=0
        for j in lst[:i]:
            if lst[i]>j:
                count+=1 
        result.append(count)
    return result
​
def right_side(lst):
    result=[]
    for i in range(len(lst)):
        count=0
        for j in lst[i:]:
            if lst[i]>j:
                count+=1 
        result.append(count)
    return result

