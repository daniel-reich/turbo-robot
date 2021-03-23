"""


Create a function that takes a two-dimensional list as an argument and returns
a one-dimensional list with the values of the original 2d list that are
arranged by spiralling through it (starting from the top-left).

### Examples

    spiral_transposition([
      [7, 2],
      [5, 0]
    ])
    
    ➞ [7, 2, 0, 5]
    
    spiral_transposition([
      [1, 2, 3],  
      [4, 5, 6],
      [7, 8, 9]
    ])
    
    ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_transposition([
      [1, 1, 1],  
      [4, 5, 2],
      [3, 3, 2] 
    ])
    
    ➞ [1, 1, 1, 2, 2, 3, 3, 4, 5]

### Notes

If you do not understand the instructions, write the 3x3 list example on a
piece of paper and trace the output through it.

"""

def spiral_transposition(my_list):
    new_list = []
​
    rows = len(my_list)
    columns = len(my_list[0])
    row = 0
    col = 0
​
    horizontal = True
    add = True
​
    while(True):
        if horizontal == True:
            if add == True:
                for i in range(columns):
                    new_list.append(my_list[row][col])
                    col += 1
​
                col -= 1
                row += 1
​
            else:
                for i in range(columns):
                    new_list.append(my_list[row][col])
                    col -= 1
​
                col += 1
                row -= 1
​
            horizontal = not horizontal
​
            rows -= 1
            if rows == 0:
                return new_list
            
        else:
            if add == True:
                for i in range(rows):
                    new_list.append(my_list[row][col])
                    row += 1
​
                row -= 1
                col -= 1
​
                add = not add
​
            else:
                for i in range(rows):
                    new_list.append(my_list[row][col])
                    row -= 1
​
                row += 1
                col += 1
​
                add = not add
​
            horizontal = not horizontal
​
            columns -= 1
            if columns == 0:
                return new_list

