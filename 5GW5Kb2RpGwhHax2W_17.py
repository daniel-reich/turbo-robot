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

def spiral_transposition(lst):
    v=len(lst)
    h=len(lst[0])
    y=x=k=0
    a=[]
    while k<h*v:        
        while x<h and lst[y][x]!='*':
            a.append(lst[y][x])
            lst[y][x]='*'
            x+=1
            k+=1
        y+=1;x-=1
        while y<v and lst[y][x]!='*':
            a.append(lst[y][x])
            lst[y][x]='*'
            y+=1
            k+=1
        x-=1;y-=1
        while x>=0 and lst[y][x]!='*':
            a.append(lst[y][x])
            lst[y][x]='*'
            x-=1
            k+=1
        x+=1;y-=1
        while y>=0 and lst[y][x]!='*':
            a.append(lst[y][x])
            lst[y][x]='*'
            y-=1
            k+=1
        if lst[y][x]=='*':
            y+=1
            x+=1
    return a

