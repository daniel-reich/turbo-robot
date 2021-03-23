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
    new_list = [0]
    position = 1
    for i in lst[1:]:
        count = 0
        index = 0
        while index < position:
            if i > lst[index]:
                count += 1
            index += 1
        new_list.append(count)
        position += 1
    return new_list
​
​
def right_side(lst):
    lst.reverse()
    new_list = left_side(lst)
    new_list.reverse()
    return new_list

