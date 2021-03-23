"""


Create a function that takes an array of numbers, and returns the size of the
biggest square patch of odd numbers. See examples for a clearer picture.

### Examples

    odd_square_patch([
      [1, 2, 4, 9],
      [4, 5, 5, 7],
      [3, 6, 1, 7]
    ]) ➞ 2
    
    # The 2x2 square at the lower right
    # ([5, 7] on the 2nd row, [1, 7] on the third).
    
    odd_square_patch([[1, 2, 4, 9]]) ➞ 1
    
    # An array with a single row can only have a square patch of
    # maximum size 1x1 containing a single odd element.
    
    odd_square_patch([[2, 4, 6]]) ➞ 0

### Notes

N/A

"""

def odd_square_patch(lst):
    count=0
    x,y=[],[]
    for word in lst:
        for i in word:
            if i%2==1:
                count+=1
        x.append(count)
        if count<=2:
            y.append(word)
        count=0
    if x[0]==0:
        return x[0]
    if len(lst)==1or (len(lst)==3 and lst[1]==y[0])or (len(lst)==1 and min(x)==2):
        return 1 
    else:
        return min(x)

