"""


Given a matrix of m * n elements (m rows, n columns), return all elements of
the matrix in spiral order.

### Examples

    spiral_order([
      [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ]
    ]) ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_order([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]) ➞ [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

### Notes

NA

"""

def spiral_order(lst):
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

