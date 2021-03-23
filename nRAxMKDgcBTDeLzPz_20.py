"""


Write a function that takes two lists (`lst1` and `lst2`) and an int `n`, and
returns `True` if the second list equals the first list shifted by `n`
positions. Otherwise, return `False`.

### Examples

    circular_shift([1, 2, 3, 4], [3, 4, 1, 2], 2) ➞ True
    
    circular_shift([1, 1], [1, 1], 6) ➞ True
    
    circular_shift([0, 1, 2, 3, 4, 5], [3, 4, 5, 2, 1, 0], 3) ➞ False

### Notes

  * The two lists will have the same length.
  * `n` can be a negative value.

"""

def circular_shift(lst1,lst2,num):
    rotate = []
    if lst1 == lst2:
        return True
    if num > 0:
        for i in range(0,len(lst1)):        # take lst2 and rotate it with num
            rotate.append(lst2[i-num])
    if num < 0:
        for i in range(0,len(lst1)):        # take lst2 and rotate it with num
            rotate.append(lst2[i+num])
    if lst1 == rotate:                  # if lst1 is equal to lst2 rotated, then we know that lst2 is the num rotated version of lst1
        return True
    else:
        return False

